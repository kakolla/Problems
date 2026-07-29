


import hashlib
from sortedcontainers import SortedList

class RingHashRouter:


    def _hash(self, string: str):
        return int(hashlib.md5(string.encode('utf-8')).hexdigest(), 16)

    def __init__(self, replicas: int = 100):
        self.replicas = replicas
        self.ring = {} # hash val -> node_id
        self.sorted_keys = SortedList()


    def add_node(self, node_id: str) -> None:
        hashes = []
        for i in range(self.replicas):
            hashes.append(self._hash(node_id + str(i)))

        # add to sorted key
        for h in hashes:
            self.sorted_keys.add(h)

            # add to ring
            self.ring[h] = node_id # point all replicas to physical node

    def remove_node(self, node_id: str) -> None:
        for i in range(self.replicas):
            h = self._hash(node_id + str(i))
            self.sorted_keys.remove(h)
            del self.ring[h]

    def get_node(self, key: str) -> str:
        hash = self._hash(key)
        pos = self.sorted_keys.bisect_left(hash)
        pos = pos % len(self.sorted_keys)

        node = self.ring[self.sorted_keys[pos]]
        return node

    def get_nodes(self, key: str, count: int) -> list[str]:
        physicals = len(set(self.ring.values()))
        count = min(count, physicals)

        x = 0
        hash = self._hash(key)
        pos = self.sorted_keys.bisect_left(hash)
        pos = pos % len(self.sorted_keys)

        all_nodes = []
        seen = set()

        while x < count:
            if self.ring[self.sorted_keys[pos]] not in seen:
                all_nodes.append(self.ring[self.sorted_keys[pos]]) # add that physical node
                seen.add(self.ring[self.sorted_keys[pos]])
                x += 1 # distinct, ignoring virutal ones that map to same

            pos += 1
            pos %= len(self.sorted_keys)

        return list(all_nodes)





router = RingHashRouter(replicas=100)
router.add_node("A")
router.add_node("B")
router.add_node("C")

# basic routing: same key always maps to same node while ring is unchanged
n1 = router.get_node("user:123")
n2 = router.get_node("user:123")
print(f"deterministic routing -> got {n1} == {n2}  [{'PASS' if n1 == n2 else 'FAIL'}]")

# replication: 2 distinct nodes for a key
nodes = router.get_nodes("user:123", 2)
print(f"get_nodes distinct count -> got {len(set(nodes))}, expected 2  [{'PASS' if len(set(nodes)) == 2 else 'FAIL'}]")

# removing a node redistributes its keys, doesn't crash, and never routes to the removed node
router.remove_node("B")
n3 = router.get_node("user:123")
print(f"node after removal != removed node -> got {n3}  [{'PASS' if n3 != 'B' else 'FAIL'}]")

for _ in range(20):
    k = f"key:{_}"
    n = router.get_node(k)
    if n == "B":
        print("FAIL: routed to removed node B")
        break
else:
    print("PASS: no keys routed to removed node B")

# load balance sanity check: with many keys and 3 nodes + virtual nodes, distribution should be roughly even
router2 = RingHashRouter(replicas=100)
router2.add_node("A")
router2.add_node("B")
router2.add_node("C")

from collections import Counter
counts = Counter(router2.get_node(f"key:{i}") for i in range(3000))
print(f"distribution across nodes -> {dict(counts)}")
# rough balance check: no node should have less than half or more than double a perfectly even share
even_share = 3000 / 3
balanced = all(even_share * 0.5 <= c <= even_share * 2 for c in counts.values())
print(f"roughly balanced -> {'PASS' if balanced else 'FAIL'}")

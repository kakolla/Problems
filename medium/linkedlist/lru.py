"""
linkedlist to keep track of most recently/least recently used with head and tail
map to get in O(1) where our nodes are for a key (key -> node)

"""
class Node:
    def __init__(self, key, val,prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.m = {} # map key -> node
        self.capacity = capacity

        self.head = None
        self.tail = None
        

    def get(self, key: int) -> int:
        if key in self.m:
            node = self.m[key]

            # move it up to head (most recently used)
            self.remove(node)
            self.add(node)
            return node.val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.m:
            # upd node
            node = self.m[key]
            node.val = value
            
            # bring it to head O(1)
            self.remove(node)
            self.add(node)
        else:
            node = Node(key, value)
            self.m[key] = node
            self.add(node)

            #evict if capacity
            if len(self.m) > self.capacity:
                del self.m[self.tail.key]
                self.remove(self.tail)
    
    # new funcs
    def add(self, node):
        # add node to head of ll
        node.prev = None
        node.next = self.head
        if self.head:
            self.head.prev = node
        self.head = node
        if not self.tail:
            self.tail = node
    def remove(self, node):
        if node.prev:
            node.prev.next = node.next
        else:
            # removing head
            self.head = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            # node is tail
            self.tail = node.prev # removed
    

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
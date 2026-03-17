from dataclasses import dataclass
@dataclass
class Shard:
    id: str
    start: int
    end: int

    """
    [start, end], [start, end]
    [X, 3, 5], [y, 3, 5], limit = 2
    - continuous
    3 5
     4 6

     3 4, 5 6
    """
       
class Shards:
    def __init__(self, limit: int):
        # Already provided (no need to implement)
        self.limit = limit
        self.shard_list: list[Shard] = []
        pass

    def add_shard(self, shard: Shard):
        # Already provided (no need to implement)
        self.shard_list.append(shard)

    def remove_shard(self, shard_id: str):
        # Already provided (no need to implement)
        for x in self.shard_list:
            if x.id == shard_id:
                self.shard_list.remove(x)
                break

    def rebalance(self):
        # TODO (you need to implement this)
        # sort based on start times
        import heapq as h
        slist: list[Shard] = sorted(self.shard_list, key = lambda x : (x.start, x.end)) # sorted list
        pq = [] # keep sorted on end times

        """
        5..10
        7 8
        8 9
        """
        for i in range(len(slist)):
            print(pq)
            curr = slist[i]
            while pq and pq[0] < curr.start:
                h.heappop(pq)
            if len(pq) < self.limit:
                h.heappush(pq, curr.end)
                continue
            else:
                # hit limit in the priority queue 
                # current shard conflicts with previous, we should alter this one
                print('rebalancing')
                curr.start = pq[0] + 1
                if curr.end < curr.start:
                    self.remove_shard(curr.id)
                    continue  # edge case where shard is instant [a,a], remove it
                h.heappush(pq, curr.end)
                # do the check again to remove
                while pq and pq[0] < curr.start:
                    h.heappop(pq)

        print("printing shards")
        print(slist)
        
if __name__ == "__main__":
    # example 2

    """
    correct logic 
    """
    s = Shards(limit=2)

    s.add_shard(Shard(id='A', start=0, end=30))
    s.add_shard(Shard(id='B', start=0, end=31))
    s.add_shard(Shard(id='C', start=0, end=32))
    s.add_shard(Shard(id='D', start=0, end=100))
    print()
    s.rebalance()

    # s = Shards(limit=1)
    # s.add_shard(Shard(id='A', start=0, end=100))
    # s.add_shard(Shard(id='B', start=80, end=180))
    # s.rebalance()



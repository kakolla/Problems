










from typing import Dict


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        from collections import Counter

        counts = Counter(tasks)
        counts = dict(sorted(counts.items(), key=lambda x: x[1], reverse=True))
        num_run = 0
        

        x = 1
        from collections import defaultdict
        scheduled = defaultdict(lambda: 0)

        import heapq
        ready = []



        while num_run < len(tasks):
            # get ready
            # counts is sorted by most frequent tasks
            for t, count in counts.items():
                if count > 0 and (scheduled[t] == 0 or scheduled[t] <= x):
                    # mark stale - not efficient
                    ready = [item for item in ready if item[1] != t]
                    heapq.heapify(ready)
                    heapq.heappush(ready, (-count, t))

            if ready:

                # newtask = ready.popleft()
                tc, newtask = heapq.heappop(ready)

                scheduled[newtask] = x + n+1
                counts[newtask] = (-tc) -1 
                num_run += 1

            if len(ready) == 0 and num_run == len(tasks):
                break


            x +=1
            

        return x


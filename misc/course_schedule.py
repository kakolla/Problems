















from collections import deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:

        # prereq is length 2

        from collections import defaultdict
        adj = defaultdict(list)

        indegree = [0 for i in range(numCourses)]   
        
        for x,y in prerequisites:
            adj[x].append(y)
        
        for i in range(numCourses):
            for j in adj[i]:
                indegree[j] += 1

            
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)


        topo = []
        while q:
            cur = q.popleft()
            topo.append(cur)

            # remove this cur
            for e in adj[cur]:
                indegree[e] -= 1
                if indegree[e] == 0:
                    q.append(e)

        print(topo)
        return len(topo) == numCourses




        

            

        











                    



        

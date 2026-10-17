





"""
dsu
- do union on the edges to get a representative for each set
- check if the src and dst are in same set 
"""


class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:

        # n vertices
        # (source, dest)


        
        parent = [i for i in range(n)]
        
        def findparent(x):
            # find this parent
            if (parent[x] != x):
                parent[x] = findparent(parent[x])
            return parent[x]
        
        # x is connected to y
        def union(x,y):
            parent[findparent(x)] = findparent(y)


        for u,v in edges:
            union(u,v)

        print(parent)
        # part of same set?
        return findparent(source) == findparent(destination)





        

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # i: adj list, n nodes
        # o: all possible paths from 0 to n-1
        n = len(graph)

        ans = []

        st = []
        st.append((0, [0])) # (node, [path])
        while st:
            node, path = st.pop()
            for out in graph[node]:
                # explore neighbors of this node
                new_path = path + [out]
                if out == n-1: # reached target 
                    ans.append(new_path)
                else:
                    st.append((out, new_path))
        
        return ans

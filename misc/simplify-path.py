








class Solution:
    def simplifyPath(self, path: str) -> str:


        tokens = path.split('/')
        print(tokens)
        st = []


        """
        split based on /
        handle . and ..


        """
        for t in tokens:
            if t == '.' or t == '':
                continue
            elif t == '..':
                if not st: continue
                st.pop()
            else:
                st.append(t)


        ans = "/" +  "/".join(st)
        return ans














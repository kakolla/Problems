class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # i: string
        # o: valid string
        # remove min num of brackets

        st = []
        remove = set()
        for i in range(len(s)):
            if s[i] == '(':
                st.append(i)
            elif s[i] == ')':
                if not st: # stack empty
                    # mark for removal
                    remove.add(i)
                else:
                    st.pop() # matched pair

        for i in st:
            remove.add(i)
        # build string
        new_s = ""
        for i in range(len(s)):
            new_s += s[i] if i not in remove else ""
        
        return new_s
            
                    
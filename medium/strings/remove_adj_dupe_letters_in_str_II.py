"""
use a stack with (letter, count)
if we match count with k, just pop it
then rebuild the string for output
"""
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # i: string s, k = k adject equal letters to delete
        # do k deletions until we can't
        # o: return final string after the process

        
        st = [] # stack (letter, count)
        for l in s:
            if not st:
                st.append((l, 1))
            elif st[-1][0] == l:
                st[-1] = (l, st[-1][1]+1)
                if st[-1][1] == k:
                    # k equal adjacent, pop it
                    st.pop()
            else:
                st.append((l, 1))
        
        res = ""
        for l, c in st:
            res += l * c
        return res
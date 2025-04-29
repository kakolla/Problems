
class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        pairs = {')': '(', '}': '{', ']': '['}

        for x in s:
            if x not in pairs:
                print("appending " + x)
                st.append(x)
            else:
                print('popping' + x)
                if len(st) == 0 or st[-1] != pairs[x]:
                    return False
                st.pop()
        
        if (len(st) == 0):
            return True
        else:
            return False

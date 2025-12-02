class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0

        c = 0
        while c < len(s):
            # odd length
            l = c
            r = c
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    ans += 1
                    l -= 1
                    r += 1
                else: break
            l = c
            r = c+1
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    ans += 1
                    l -= 1
                    r += 1
                else: break

            c += 1
        
        return ans

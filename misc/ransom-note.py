








class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:


        c = {}
        # freq
        for l in magazine:
            c[l] = c.get(l, 0) + 1

        for l in ransomNote:
            if c.get(l, 0) == 0:
                return False
            else:
                c[l] -= 1

        return True

      








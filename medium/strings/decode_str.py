class Solution:
    def rec(self, s: str, i: int) -> tuple[str, int]:

        # extract number, then recursive call
        num = ""
        result = ""
        while i < len(s) and s[i] != ']':
            if s[i].isdigit():
                num = ""
                while s[i].isdigit():
                    num += s[i]
                    i += 1
                num = int(num)
                i +=1 # skip bracket
                # recursive call
                # to get the following string that should be repeated 
                following_s, i = self.rec(s, i)
                result += num * following_s
            else:
                result += s[i] # add letters
                i += 1
        return (result, i+1) # skip the ']'

    def decodeString(self, s: str) -> str:
        # i: encoded str
        # o: decoded str

        decoded, _ = self.rec(s, 0)
        return decoded

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # if s is subseq of t, t is larger

        i = 0 # char index of s
        j = 0 # char index of t
        while j < len(t):
            if i < len(s) and s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1 # t moves forward
        
        # if we are able to match all the letters in s
        return i == len(s)
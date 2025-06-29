class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        vowels = 0
        v = "aeiou"

        # count vowels in first window
        for i in range(0, k):
            if s[i] == "a" or s[i] == "e" or s[i] == "i" or s[i] == "o" or s[i] == "u":
                vowels += 1

        maxn = vowels
        l = 0
        r = k
        # count vowels in sliding window
        while r < n:
            print(vowels)
            if s[r] == "a" or s[r] == "e" or s[r] == "i" or s[r] == "o" or s[r] == "u":
                vowels += 1
            if s[l] == "a" or s[l] == "e" or s[l] == "i" or s[l] == "o" or s[l] == "u":
                vowels -= 1
            
            maxn = max(vowels, maxn)
            r += 1
            l += 1
        
        return maxn

 
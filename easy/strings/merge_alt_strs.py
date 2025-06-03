class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        for a, b in zip(word1, word2):
            result += a
            result += b
        
        result += word1[len(word2):]
        result += word2[len(word1):]
        return result

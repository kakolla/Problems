class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        l1 = len(word1)
        l2 = len(word2)
        result = ""
        w1done = False
        w2done = False

        while True:
            if i >= l1 and j >=l2:
                w1done = True
                w2done = True
                break
            elif i >= l1:
                w1done = True
                break
            elif j >= l2:
                w2done = True
                break
            result += word1[i]
            result += word2[j]
            i += 1
            j += 1

        if w1done and not w2done:
            result += word2[j:]
        elif not w1done and w2done:
            result += word1[i:] 
        
        return result

        
        
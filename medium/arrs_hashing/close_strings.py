

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        # letters used must match in both
        p1 = {}
        p2 = {}

        # count occurrences 
        for l in word1:
            p1[l] = p1.get(l, 0) + 1
        for l2 in word2:
            p2[l2] = p2.get(l2, 0) + 1
        
        # construct a set
        s1 = sorted(p1.values()) # sort the frequencies
        s2 = sorted(p2.values()) # sort 
        letters_used1 = p1.keys()
        letters_used2 = p2.keys()

        # make sure its using the same letters
        # and sorted freqs match
        return s1 == s2 and letters_used1 == letters_used2

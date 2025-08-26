from typing import List
from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []

        l = 0
        r = len(p)

        # get freq map of p
        f = Counter(p)

        while r <= len(s):

            


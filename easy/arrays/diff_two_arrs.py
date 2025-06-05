from typing import List
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans = []
        s1 = set(nums1)
        s2 = set(nums2)
        ans.insert(0, list(s1 - s1.intersection(nums2)))
        ans.insert(1, list(s2 - s2.intersection(nums1)))

        return ans


        
        
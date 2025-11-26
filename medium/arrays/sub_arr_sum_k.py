class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # i: list of ints, k
        # o: number of subarrs with sum of k

        
        # get prefix sums
        prefs_map = {0: 1} # count of how many times we see this pref sum
        count = 0
        prefix = 0

        """
        sum(i,j) = pref[j] - pref[i] = k
        pref[i] = pref[j] - k
        how many pref sums equal to rhs
        """

        # count prefix sums and check subarrays 
        for num in nums:
            prefix += num
            check = prefix - k
            if check in prefs_map:
                count += prefs_map.get(check)
            prefs_map[prefix] = prefs_map.get(prefix, 0) + 1
        

        return count
    
class Solution:
    def maxOperations(self, s: str) -> int:
        # i: binary string
        # o: max ops to move ones to the end

        n = len(s)
        
        ones_seen = 0
        ops = 0
        for i in range(n):
            if s[i] == '1': ones_seen += 1
            if i+1 <n and s[i:i+2] == '10':
                # add however many 1s we've seen, 
                # bc those have to cross this 0 
                ops += ones_seen
        
        return ops

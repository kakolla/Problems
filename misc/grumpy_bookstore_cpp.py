



class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        # return max num of customers tht can be satisfied



        # 1,0,1,2,1,1,7,5
        # 0,1,0,1,0,1,0,1
        
        max_seen = 0
        mc =0

        if minutes > len(customers):
            return mc
 
        # get max
        for i in range(len(customers)):
            if grumpy[i] == 0:
                mc += customers[i]
       
        # in window, add up the ones that are grumpy, would make it ungrumpy
        for i in range(minutes):
            if grumpy[i] == 1:
                mc += customers[i]
                max_seen = max(max_seen, mc)
            


        l, r = 1, minutes
        while r < len(customers):
            mc -= customers[l-1] if grumpy[l-1] else 0
            # mc -= customers[r-1] if grumpy[l-1] else 0
            if r == len(customers): break
            # mc  += customers[l] if grumpy[l] else 0

            mc  += customers[r] if grumpy[r] else 0
            max_seen = max(max_seen, mc)
            l += 1
            r += 1


        return max_seen








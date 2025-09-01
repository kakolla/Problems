class Solution:

    def rec(self, x: float, n: int) -> float:
        if n == 2:
            return x * x
        if n == 1:
            return x
        if n == 0:
            return 1


        if n % 2 == 0:
            # even
            t = self.rec(x, n//2)
            return t * t 
        else:
            # odd
            return x * self.rec(x, n-1)
        


    def myPow(self, x: float, n: int) -> float:
        # x * x * ... n times
        # 2^10 = (2^5) * ( 2^5)
        # 2^5 = (2)(2^4)
        # this is d&q

        if n < 0:
            return 1/ self.rec(x, -n)
        else:
            return self.rec(x, n)





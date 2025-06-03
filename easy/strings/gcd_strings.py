class Solution:
    def gcd(self, a, b) -> str:

        # Euclidean algorithm
        while (a != b):
            if (a > b):
                a = a-b
            elif (a < b):
                b = b-a
        return a

        

        
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # early exit
        # there is no common divisor
        # t + t + .. t doesn't exist
        if str1 + str2 != str2 + str1:
            return ""
        
        # at this point, there is a repeating string every q letters
        q = self.gcd(len(str1), len(str2))
        return str1[:q]
        











from collections import defaultdict



class Solution:


    def letterCombinations(self, digits: str) -> list[str]:

        l = "abcedfghijklmnopqrstuvwxyz"
        maps = defaultdict(str)

        
        j = 0
        for i in range(2, 10):
            maps[i]= (l[j:j+3])
            j += 3

        for k,v in maps.items():
            print (k, v )


        ans = []
        maps[7] = "pqrs"
        maps[8] = "tuv"
        maps[9] = "wxyz"


        def rec(n, curr):
            if (n == len(digits)):
                ans.append(curr)
                return
            d = int(digits[n])

            for letter in maps[d]:
                rec(n+1, curr + letter)

           

        rec(0, "")
        return ans



        

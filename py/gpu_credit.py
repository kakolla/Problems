"""
can come out of order
ie usecredit before adding credit

best case: add credit, use credit
case:  usecredit, getbalance, addcredit @ same timestamp
"""
from collections import defaultdict
class GPUCredit:
    credits = defaultdict(list)
    adds = []
    uses = []

    def addCredit(self, creditID: str, amount: int, timestamp: int, expiration: int) -> None:
        # A credit is an offering of GPU balance that expires after some expiration-time.
        #  The credit can be used only during [timestamp, timestamp + expiration]. 
        # **Check with your interviewer whether this period is inclusive '[]' or exclusive '()'.
        #  Examples given were inclusive.** A credit can be repeatedly used until expiration.

        self.adds.append((amount, timestamp, expiration+timestamp))
    def useCredit(self, timestamp: int, amount: int) -> None:
        # use the credit that would expire soonest
        self.uses.append((amount, timestamp))

    def getBalance(self, timestamp: int) -> int | None: 
        # return the balance remaining on the account 
        #at the timestamp, return None if there are no credit left. Note, balance cannot be negative. 
        # See edge case below.
        
        balance = 0
        adds_copy = [list(a) for a in self.adds]
        adds_copy.sort(key= lambda x: x[2]) # sort on closest expiration 
       
        sorted_uses = sorted(self.uses, key= lambda x: x[1]) # sort on time used
        
        for amt, time in sorted_uses:
            if time > timestamp: continue

            # use from credits until none left
            for i in range(len(adds_copy)):
                cred_amt, cred_start, cred_end = adds_copy[i]
                if cred_start <= time <= cred_end:
                    # within timestamp, use it
                    useup = min(adds_copy[i][0], amt)
                    adds_copy[i][0] -= useup
                    # use all, or some leftover
                        # in that case, use it with next credit  in the adds array
                    amt -= useup # update


        found = False
        for amt, start, end in adds_copy:
            if start <= timestamp <= end:
                found = True
                balance += amt
        return  balance if found else None
                



# gpuCredit = GPUCredit()
# gpuCredit.addCredit('microsoft', 10, 10, 30)
# print(gpuCredit.getBalance(0)) # returns None
# print(gpuCredit.getBalance(10)) # returns 10
# print(gpuCredit.getBalance(40)) # returns 10
# print(gpuCredit.getBalance(41)) # returns None

gpuCredit = GPUCredit()
print(gpuCredit.addCredit('amazon', 40, 10, 50))
print(gpuCredit.useCredit(30, 30))
print(gpuCredit.getBalance(40)) # returns 10
print(gpuCredit.addCredit('google', 20, 60, 10))
print(gpuCredit.getBalance(60)) # returns 30
print(gpuCredit.getBalance(61)) # returns 20
print(gpuCredit.getBalance(70)) # returns 20
print(gpuCredit.getBalance(71)) # returns None
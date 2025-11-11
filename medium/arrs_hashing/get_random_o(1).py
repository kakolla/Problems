"""
use an array adjacent to hash map to keep track of positions,
use the array to return random number in O(1)
"""
class RandomizedSet:

    def __init__(self):
        self.s = {}
        self.arr = []
        

    def insert(self, val: int) -> bool:
        # insert val into set
        if val in self.s:
            return False
        self.s[val] = len(self.arr) # index
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        if self.s.get(val, -1) != -1:
            cond = True
            index = self.s[val]
            # swap last and element
            self.arr[index] = self.arr[len(self.arr)-1] 
            self.s[self.arr[index]] = index # update index
            self.arr.pop() # remove last number -- O(1)
            self.s.pop(val) # remove dictionary key
        else: cond = False

        return cond
    
    def getRandom(self) -> int:
        import random
        n = random.randint(0, len(self.arr)-1)
        return self.arr[n]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
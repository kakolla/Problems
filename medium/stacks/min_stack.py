"""
maintain 2 stacks, regular stack and one that tracks the min seen
all operations are O(1)
"""
class MinStack:

    def __init__(self):
        self.st = []
        self.min = []

    def push(self, val: int) -> None:
        if self.min:
            self.min.append(min(self.min[-1], val))
        else:
            self.min.append(val)
        self.st.append(val)
        

    def pop(self) -> None:
        self.st.pop()
        self.min.pop()
        

    def top(self) -> int:
        return self.st[-1]
        

    def getMin(self) -> int:
        return self.min[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
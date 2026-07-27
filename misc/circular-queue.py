







class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.front = 0
        self.arr = [0 for i in range(k)]
        self.count = 0
        

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        r = self.front + self.count
        next_slot = r % self.k
        self.arr[next_slot] = value
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        self.front = (self.front + 1) % self.k
        self.count -= 1
        return True
        
    def Front(self) -> int:
        if self.isEmpty(): return -1
        return self.arr[self.front]
        

    def Rear(self) -> int:
        if self.isEmpty(): return -1
        return self.arr[(self.front + self.count - 1)% self.k]
        

    def isEmpty(self) -> bool:
        return self.count == 0
        

    def isFull(self) -> bool:
        return self.count == self.k
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

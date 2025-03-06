
class FibIterator:
    def __init__(self, max):
        self.max = max
        self.a = 0
        self.b = 1
        self.count = 0

    
    def __iter__(self):
        return self

    def __next__(self):
        if (self.count >= self.max):
            raise StopIteration

        temp = self.a
        self.a = self.b
        self.b = temp + self.b
        self.count += 1
        return self.a


if "__main__" == __name__:
    it = FibIterator(5)
    for x in it:
        print(x)

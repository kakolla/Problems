
class Fib:

    def __init__(self, max):
        print("init is" + str(max))
        self.max = max
        self.a = 1
        self.b = 1
        self.count = 0
        

    def __iter__(self):
        return self

    def __next__(self):
        if self.count > self.max:
            raise StopIteration
        
        # 1 1 2 3 5 8 ...
        temp = self.a
        self.a = self.b
        self.b = self.b + temp
        self.count += 1
        return self.a


if "__main__" == __name__:
    max = 10
    fib = Fib(max)
    for i in range(max):
        print(fib.a)
        next(fib)

    newit = Fib(max)
    for x in newit:
        print(x, end=' ')


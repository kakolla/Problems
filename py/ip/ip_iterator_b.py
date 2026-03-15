"""
Design a class IPv4Iterator that iterates through a range of IPv4 addresses,
 inclusive of both start_ip and end_ip. An IPv4 address is a string in the format 
 "A.B.C.D" where 0 <= A, B, C, D <= 255.
"""

class IPv4Iterator:
    def __init__(self, start_ip: str, end_ip: str, increasing: bool = True):
        """Initializes the iterator to start at start_ip and end at end_ip (inclusive)."""
        # set start and end here
        self.incr = increasing
        if increasing:
            self.curr = [int(i) for i in start_ip.split('.')] # a,b,c,d
            self.end = [int(i) for i in end_ip.split('.')]
            if not self.check_range(self.curr): raise ValueError("noth eld")
        else:
            self.curr = [int(i) for i in start_ip.split('.')]
            self.end = [int(i) for i in end_ip.split('.')] 
            if not self.check_range(self.curr): raise ValueError("noth eld")

    def get_next(self, curr: list[int]) -> list[int]:
        i = -1
        next = curr[::]
        if self.incr:
            next[i] += 1 # add 1 to d
            while i >= (-1 * len(curr)) and next[i] > 255:
                next[i] = 0 
                next[i-1] += 1
                i -= 1
        else:
            next[i] -= 1
            while i >= (-1 * len(curr)) and next[i] < 0:
                next[i] = 255
                next[i-1] -= 1 # borrow
                i -= 1

        return next
    
    def ip(self, ip: list[int]) -> int:
        a,b,c,d = ip
        # a.b.cd. -> int representation
        # a << 24
        return (a << 24) | (b << 16) | (c << 8) | d # return integer 

    def check_range(self, curr: list[int]) -> bool:
        if self.incr:
            return self.ip(curr) <= self.ip(self.end)
        else:
            return self.ip(curr) >= self.ip(self.end)


    def hasNext(self) -> bool:
        """Returns True if there is another IP in the range, else False."""
        # check and erturn
        # get the next one
        next_ip = self.get_next(self.curr)
        return self.check_range(next_ip)

    def next(self) -> str:
        """Returns the next IP in the range. Raises StopIteration if no more IPs."""
        # if next, return current and move forward
        if self.hasNext():
            self.curr = self.get_next(self.curr) # set curr to nexrt
            s = ""
            for i in self.curr:
                s += str(i) + "."
            return s[:-1]
        else:
            raise StopIteration()

if __name__ == "__main__":
    # ipv4 = IPv4Iterator("255.255.14.255", "255.255.15.2")
    # print(ipv4.hasNext()) # True
    # print(ipv4.next()) # "255.255.14.255"
    # print(ipv4.next()) # "255.255.14.256" is invalid — actually wraps to "255.255.15.0"
    # print(ipv4.next()) # "255.255.15.1"
    # # print(ipv4.next()) # "255.255.15.2"
    # print(ipv4.hasNext()) # False
    # ipv4.next() # Raises StopIteration

    ipv4 = IPv4Iterator("255.255.15.2","255.255.14.250", increasing=False)
    print(ipv4.hasNext()) # True
    print(ipv4.next()) # "255.255.14.255"
    print(ipv4.next()) # "255.255.14.256" is invalid — actually wraps to "255.255.15.0"
    print(ipv4.next()) # "255.255.15.1"
    print(ipv4.next()) # "255.255.15.1"
    print(ipv4.next()) # "255.255.15.1"
    print(ipv4.next()) # "255.255.15.1"
    print(ipv4.next()) # "255.255.15.1"
    print(ipv4.next()) # "255.255.15.1"
    # print(ipv4.next()) # "255.255.15.2"
    print(ipv4.hasNext()) # False
    # ipv4.next() # Raises StopIteration
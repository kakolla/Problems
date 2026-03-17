"""
Design a class IPv4Iterator that iterates through a range of IPv4 addresses,
 inclusive of both start_ip and end_ip. An IPv4 address is a string in the format 
 "A.B.C.D" where 0 <= A, B, C, D <= 255.
"""

class IPv4Iterator:
    def get_ip_num(self, ip: list[int]):
        # take ip and return integer representation
        a,b,c,d = ip
        return (a << 24) | (b << 16) | (c<< 8) | d
    def get_ip_from_num(self, num) -> list[int]:
        # 11111111 11111111
        a = (num >> 24) & (0x00ff)
        b = (num >> 16) & (0x00ff)
        c = (num >> 8) & (0x00ff)
        d = (num ) & (0x00ff)
        
        return [a,b,c,d]

    def __init__(self, ip: str):
        """ip with subnet mask"""
        self.ip = ip
        # get network ip
        temp = ip.split('/')
        self.network_ip: str = temp[0]
        self.mask_num: int = int(temp[1]) # 1111100, (-1) << 8 


        network = [int(i) for i in self.network_ip.split('.')]
        self.network_num = self.get_ip_num(network)
        self.mask = (-1) << (32 - self.mask_num)

        t = self.network_num & self.mask
        start: list[int] = self.get_ip_from_num(t)
        end_num = self.network_num | ~(self.mask)
        end: list[int] = self.get_ip_from_num(end_num)
        self.curr = start
        self.end = end


        """
        network_start = ip & mask
        network_end = network_start | ~(mask)
        
        """


    def get_next(self, curr: list[int]) -> int:
        i = -1
        next = curr[::]
        next[i] += 1 # add 1 to d
        while i >= (-1 * len(curr)) and next[i] > 255:
            next[i] = 0 
            next[i-1] += 1
            i -= 1
        return next
    
    def check_range(self, curr: list[int]) -> bool:
        return self.get_ip_num(curr) <= self.get_ip_num(self.end)
        # return self.get_next(self.get_ip_num(curr)) <= 
        # for i in range(4):
        #     if curr[i] > self.end[i]:
        #         return False
        # return True


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
    
    def __iter__(self):
        return self
    def __next__(self):
        return self.next()

if __name__ == "__main__":
    ipv4 = IPv4Iterator("192.168.1.0/24")
    for i in ipv4:
        print(i)
    # print(ipv4.hasNext()) # True
    # print(ipv4.next()) # "255.255.14.255"
    # print(ipv4.next()) # "255.255.14.256" is invalid — actually wraps to "255.255.15.0"
    # print(ipv4.next()) # "255.255.15.1"
    # # print(ipv4.next()) # "255.255.15.2"
    # print(ipv4.hasNext()) # False
    # # ipv4.next() # Raises StopIteration
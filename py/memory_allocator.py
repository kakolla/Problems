"""
Implement a class to simulate memory allocation. Upon initialization, the class receives a total memory size. 
It must support the following two operations:

allocate(size: int) -> int: Allocate a contiguous block of memory of the given size. Return the starting address
 of the allocated block. If allocation is not possible, raise an error.
free(address: int, size: int): Free a previously allocated block of memory starting from the given address with the
 specified size. If the operation is invalid (e.g., the block was not allocated or overlaps incorrectly), raise an error.
All memory allocations must be contiguous.

"""
class Memory:
    """SIMULATE memory allocation"""
    def __init__(self, total_size: int):
        self.total_size = total_size
        self.brk = total_size-1 # end address
        self.m = [0] * total_size # each entry is a byte (or unit of space)
    
    def allocate(self, size: int) -> int:
        # allocate contiguous block of memory
        # scan list for free block
        
        for i in range(len(self.total_size)):
            if self.m[i] == 0 and self.m[i+size] == 0:
                # there is space
                # 0...0
            elif 



    
    def free(self, address: int, size: int):
        # start from addr for specific size, 
        

# cases:
# no space, so have to extend the heap
# size = 4 
# 11


        


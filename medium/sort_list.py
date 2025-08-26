# first solve using hashmap & regular sorting (uses memory)
# second solve - d&q merge sort

from typing import Optional 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        m = {}
        curr = head
        while curr != None:
            m[curr.val] = m.get(curr.val, [])
            m[curr.val].append(curr) # val -> node ptr

            curr = curr.next

        m_sorted = sorted(m.items(), key=lambda x: x[0])


        # stitch back
        curr = None
        prev = None
        head = None
        m_sorted = [k[1] for k in m_sorted]
        for n in m_sorted:
            for j in n:
                if head == None:
                    head = j
                    prev = j
                else:
                    curr = j
                    curr.next = None
                    prev.next = curr
                    prev = j
        

        return head
        

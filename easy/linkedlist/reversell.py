# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rec(self, prev, curr):
        if curr is None:
            return prev
        n = curr.next
        curr.next = prev
        return self.rec(curr, n)

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return head
        

        t = head.next
        head.next = None
        return self.rec(head, t)
        

        
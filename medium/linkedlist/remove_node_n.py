# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # list of size 1
        if head == None:
            return head

        fast = head
        slow = head


        # advance fast pointer n steps ahead
        # i.e. if n = 3rd from the last
        # when fast ptr hits the end, slow ptr will be 
        # before the elem that needs to be deleted (3rd from last)
        for i in range(n):
            if fast:  
                fast = fast.next

        # if we jumped all the way to the end,
        # we have to delete the head
        if fast is None:
            return head.next

        # advance the ptrs
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        
        # next node is the one we have to delete
        slow.next = slow.next.next
        
        return head


"""
1 2 3 4 5
11
23
35


"""
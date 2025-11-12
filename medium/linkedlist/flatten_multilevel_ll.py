"""
use dfs, which returns the TAIL ptr of the flattened list to join
lot of pointer thinking
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        
        def dfs(node):
            
            cur = node

            while cur:
                # flatten if we have a child
                nxt = cur.next
                if cur.child:
                    tail = dfs(cur.child)
                    temp_next = cur.next
                    cur.next = cur.child
                    cur.child = None
                    cur.next.prev = cur
                    if temp_next:
                        tail.next = temp_next
                        temp_next.prev = tail
                    last = tail
                else:
                    last = cur
                cur = nxt # keep going
            return last
        
        dfs(head)
        return head
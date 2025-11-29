"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        # get path
        p_path = set()
        curr = p
        while curr:
            p_path.add(curr)
            curr = curr.parent
        
        curr = q
        while curr:
            if curr in p_path:
                return curr
            curr = curr.parent
        
        
        
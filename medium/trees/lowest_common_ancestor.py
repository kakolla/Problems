# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rec(self, node, p, q):
        if not node:
            return None
        
        if node == p or node == q:
            return node
        
        # check left and right for p or q
        left_subtree = self.rec(node.left, p, q)
        right_subtree = self.rec(node.right, p, q)

        if left_subtree and right_subtree:
            return node # first node we see that has both p & q
        
        # if one or the other, return those
        return left_subtree or right_subtree
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.rec(root, p, q)
        
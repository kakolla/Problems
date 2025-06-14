# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_height(self, node: TreeNode) -> int:
        if not node:
            return 0
        
        l = self.get_height(node.left)
        r = self.get_height(node.right)
        h = 1 + max(l,r)
        return h

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.get_height(root)
        
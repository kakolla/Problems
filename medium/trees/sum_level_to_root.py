# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node: TreeNode, num: str) -> int:
        if not node.left and not node.right:
            # leaf node
            print(num)
            return int(num)
        
        s = 0
        if node.left:
            s += self.dfs(node.left, num + str(node.left.val))
        if node.right:
            s += self.dfs(node.right, num + str(node.right.val))

        return s
    
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        return self.dfs(root, str(root.val))
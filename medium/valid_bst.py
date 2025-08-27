import sys
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:

    def recurse(self, node: TreeNode | None, low: int, high: int) -> bool:

        # for a curr node, check if left < curr < right and 
        # make sure left and right subtree are within the low, high bounds we pass
        # the recursion
        if node == None:
            return True
        

        left = self.recurse(node.left, low, node.val)
        right = self.recurse(node.right, node.val, high)

        # check left < curr < right
        if node.left and node.right:
            valid = node.left.val < node.val and node.right.val > node.val
            valid = valid and (node.left.val > low and node.left.val < high) and (node.right.val > low and node.right.val < high)
        else:
            if node.left == None and node.right:
                valid = node.right.val > node.val
                valid = valid and (node.right.val < high and node.right.val > low)
            if node.left and node.right == None:
                valid = node.left.val < node.val
                valid = valid and (node.left.val < high and node.left.val > low)
            elif not node.left and not node.right:
                valid = True # no children


        return valid and left and right



    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return False
        
        return self.recurse(root, -sys.maxsize - 1, sys.maxsize)
        
        


        
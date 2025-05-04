# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:   
    def isSameTree(self, root1, root2):
        if not root1 and not root2 :
            return True
        if not root1 or not root2:
            return False 

        # check if the two trees are identifcal in struc & vals    
        leftIdentical = self.isSameTree(root1.left, root2.left)
        rightIdentical = self.isSameTree(root1.right, root2.right)
        return leftIdentical and rightIdentical and root1.val == root2.val
    


        


    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        # while root is not null
    
        if not self.isSameTree(root, subRoot):
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        else:
            return True




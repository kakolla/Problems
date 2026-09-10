



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        st = []

        ans = []

        st.append((root, False)) # node, visited
        
        while st:
            top, visited = st.pop()
            if visited:
                ans.append(top.val)
            else:
                if top is None:
                    continue
                if top.left is None and top.right is None:
                    ans.append(top.val)
                    continue
                st.append((top, True))
                st.append((top.right, False))
                st.append((top.left, False))

        return ans




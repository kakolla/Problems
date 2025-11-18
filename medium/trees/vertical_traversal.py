"""
looks like in order traversal but nah
do BFS and keep track of column we are at. if left, col -1, if right col +1
then build view starting from lowest col and go up

"""
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        from collections import deque, defaultdict
        q = deque()
        q.append((root, 0)) # node, col #
        cols = defaultdict(list)
        
        min_col = float('inf')
        max_col = float('-inf')
        while q:
            f, f_col = q.popleft()
            min_col = min(min_col, f_col)
            max_col = max(max_col, f_col)
            cols[f_col].append(f.val)
            if f.left:
                q.append((f.left, f_col-1))
            if f.right:
                q.append((f.right, f_col+1))
        
        # build vertical view starting from min val
        ans = []
        for i in range(min_col, max_col+1):
            ans.append(cols[i])
        return ans



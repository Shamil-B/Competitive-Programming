# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        arr = []
        min_ = inf
        def solve(root):
            if not root:
                return

            solve(root.left)
            arr.append(root.val)
            solve(root.right)
            
        solve(root)
        for i in range(1,len(arr)):
            min_ = min(min_,arr[i]-arr[i-1])

        return min_
                
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def solve(root):
            if not root:
                return 0
            
            sum_ = root.val if root.val >= low and root.val <= high else 0
            if root.left:
                sum_ += solve(root.left)

            if root.right:
                sum_ += solve(root.right)

            return sum_

        return solve(root)

            
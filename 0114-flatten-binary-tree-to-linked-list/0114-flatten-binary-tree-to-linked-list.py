# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        def solve(node):
            
            if not node or not node.left and not node.right:
                return node

            prev_right = node.right
            tail = node
            if node.left:
                node.right = node.left
                tail = solve(node.left)
                node.left = None

            if prev_right:
                tail.right = prev_right
                tail = solve(prev_right)

            return tail
        
        solve(root)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        # the choice is me or my grandchildren
        
        memo = {}
        def dp(node):
            
            if not node:
                return 0
            
            if node and not node.right and not node.left:
                return node.val
            
            if node not in memo:
                gc1 = None if not node.left else node.left.left
                gc2 = None if not node.left else node.left.right
                gc3 = None if not node.right else node.right.left
                gc4 = None if not node.right else node.right.right
                
                memo[node] = max(sum([node.val,dp(gc1),dp(gc2),dp(gc3),dp(gc4)]),dp(node.left)+dp(node.right))
                
            return memo[node]
                
        return dp(root)
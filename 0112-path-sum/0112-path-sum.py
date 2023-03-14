# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.found = False
        def backtrack(root,curSum,target):
            
            if self.found or not root:
                return
            
            if root and not root.left and not root.right:
                curSum += root.val
                
                if curSum == targetSum:
                    self.found = True

            curSum += root.val
            
            backtrack(root.left,curSum,target)
            backtrack(root.right,curSum,target)
            
        backtrack(root,0,targetSum)
        
        return self.found
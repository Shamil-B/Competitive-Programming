# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode],isTop=True) -> bool:
        
        if not root:
            return True
        
        if not root.left and not root.right:
            return 1
        
        left = right = -1
        if root.left:
            left = self.isBalanced(root.left,False)
            
        if root.right:
            right = self.isBalanced(root.right,False)
            
        if left==False or right==False:
            return False
            
        left = 0 if left==-1 else left
        right = 0 if right==-1 else right
        if abs(right-left) > 1:
            return False
        
        if isTop:
            return True
        
        return 1 + max(left,right)
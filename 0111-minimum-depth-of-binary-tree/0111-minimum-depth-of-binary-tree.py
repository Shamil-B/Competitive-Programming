# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode],isTop=True) -> int:
        
        if not root:
            return 0
        
        if (root.left and root.right):
            left = self.minDepth(root.left,False)
            right = self.minDepth(root.right,False)

            return 1 + min(left,right)
        
        else:
            if root.left:
                return 1+self.minDepth(root.left)
            
            return 1+self.minDepth(root.right)
        
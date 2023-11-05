# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.sum = 0
        
        def traverse(node,add):
            if not node:
                return
            
            if node and not node.left and not node.right:
                if add:
                    self.sum += node.val
                return
            
            traverse(node.left,True)
            traverse(node.right,False)
            
        traverse(root,False)
        return self.sum
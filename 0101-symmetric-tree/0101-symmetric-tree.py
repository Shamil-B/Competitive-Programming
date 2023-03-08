# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool: 
        if not root:
            return True
        
        self.left = []
        self.right = []
        
        if root.left and root.right and root.left.val != root.right.val:
            return False
        
        #iterate left node right then right node left
        
        def helper(root,forward=True):
            if forward:
                if not root: 
                    self.left.append(None)
                    return
                
                if not root.left and not root.right:
                    self.left.append(root.val)
                    return 
                
                helper(root.left)
                self.left.append(root.val)
                helper(root.right)
                
            else:
                if not root: 
                    self.right.append(None)
                    return
                
                if not root.left and not root.right:
                    self.right.append(root.val)
                    return 
                
                helper(root.right,False)
                self.right.append(root.val)
                helper(root.left,False)
        
        helper(root)
        helper(root,False)
        
        return self.left == self.right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.num = []
        def backtrack(s,root):
            
            if root and not root.left and not root.right:
                s += str(root.val)
                self.num.append(s)
                return
            
            if not root:
                return
            
            s += str(root.val)
            
            backtrack(s,root.left)
            backtrack(s,root.right)
            
        backtrack("",root)
        return sum(list(map(int,self.num)))
        
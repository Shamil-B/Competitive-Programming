# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #traverse in order
        self.k = k
        self.ans = None
        def helper(root):
            
            if not root:
                return
            
            left = helper(root.left)            

            self.k-=1
            if self.k==0:
                self.ans = root
                
            right = helper(root.right)

            
        helper(root)
        return self.ans.val

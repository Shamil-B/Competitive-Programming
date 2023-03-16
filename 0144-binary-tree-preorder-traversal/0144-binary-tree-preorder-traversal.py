# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        self.nums = []
        def traversePre(node):
            
            if not node:
                return
            
            self.nums.append(node.val)
            
            traversePre(node.left)
            traversePre(node.right)
            
        traversePre(root)
        return self.nums
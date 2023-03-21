# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.pot = []
        
        def traversePostOrder(node):
            
            if not node:
                return
            
            traversePostOrder(node.left)
            traversePostOrder(node.right)
            
            self.pot.append(node.val)
            
        traversePostOrder(root)
        return self.pot
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def traverse(node):
            if not node:
                return ""

            cur = str(node.val)
            left = traverse(node.left)
            if left:
                cur += "("+(left)+")"

            right = traverse(node.right)
            if right:
                if not left:
                    cur += "()"
                cur += "("+(right)+")"
                
            return cur
        return traverse(root)
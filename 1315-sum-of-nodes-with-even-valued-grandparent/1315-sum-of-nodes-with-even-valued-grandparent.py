# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        stack = []
        sum_ = 0
        def traverse(node,parent):
            nonlocal sum_
            if not node:
                return
                
            if parent:
                sum_ += (node.left.val if node.left else 0) + (node.right.val if node.right else 0)
                
            parent = node.val%2==0
            
            traverse(node.left,parent)
            traverse(node.right,parent)
            
        traverse(root,False)
        return sum_
            
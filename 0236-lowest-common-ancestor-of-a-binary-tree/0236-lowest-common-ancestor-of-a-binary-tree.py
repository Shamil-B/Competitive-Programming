# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def solve(root):
            if not root:
                return False, None

            leftSingleFound, leftAns = solve(root.left)
            rightSingleFound, rightAns = solve(root.right)

            current = False
            if root.val == p.val or root.val == q.val:
                current = True
                
            if leftAns:
                return True, leftAns
            
            if rightAns:
                return True, rightAns
            
            if (leftSingleFound and rightSingleFound) or (current and rightSingleFound) or (leftSingleFound and current):
                return True, root

            return leftSingleFound or rightSingleFound or current, None

        return solve(root)[1]
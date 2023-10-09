# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None
        def solve(root):
            if not root:
                return False

            left = solve(root.left)
            right = solve(root.right)

            current = False

            if root.val == p.val or root.val == q.val:
                current = True

            if ((left and right) or (left and current) or (right and current) and not self.ans):
                self.ans = root

            return left or right or current

        solve(root)
        return self.ans
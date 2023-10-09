# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        self.dic = set()
        self.ans = []
        used = set()
        def solve(root):
            if not root:
                return ""
            
            left = solve(root.left)
            right = solve(root.right)

            if not left and right:
                left = "#"
                
            if not right and left:
                right = "#"

            curString = str(root.val) + "." + left + "." + right
            if curString in self.dic and curString not in used:
                self.ans.append(root)
                used.add(curString)

            else:
                self.dic.add(curString)

            return curString

        solve(root)
        return self.ans
                
                
            
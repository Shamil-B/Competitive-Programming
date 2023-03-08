# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        self.freq = {}
        def helper(root):
            if not root:
                return
            
            helper(root.left)
            
            if root.val not in self.freq:
                self.freq[root.val] = [1,root.val]
                
            else:
                self.freq[root.val][0] += 1
            
            helper(root.right)
            
        helper(root)
        result = []
        values = list(self.freq.values())
        maxx = max(values)

        for val in values:
            if val[0]==maxx[0]:
                result.append(val[1])
                
        return result
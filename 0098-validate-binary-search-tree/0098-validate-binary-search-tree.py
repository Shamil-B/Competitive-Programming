# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:        
        
        def helper(root):
            # (min,max)
            if not root:
                return (inf,-inf,True)

            leftMin,leftMax,ansL = helper(root.left)
            rightMin,rightMax,ansR = helper(root.right)
            
            val = leftMax < root.val < rightMin
                
            return (min(root.val,leftMin),max(root.val,rightMax),(ansL and ansR and val))
        
        return helper(root)[2]            
            
        
            
        
            
        
        
#         left = right = []
        
#         if not root.left and not root.right:
#             return [root.val]
        
#         if root.left:
#             left = self.isValidBST(root.left,False)
            
#         if root.right:
#             right = self.isValidBST(root.right,False)
            
            
#         if isTop:
#             res = left + [root.val] + right
#             return self.isSorted(res)
        
#         return left + [root.val] + right
    
    
#     def isSorted(self,arr):
#         for i in range(1,len(arr)):
#             if arr[i]<=arr[i-1]:
#                 return False
            
#         return True
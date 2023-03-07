# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.res = True
        
        
        def helper(root):
            # (min,max)
            if not root:
                return (inf,-inf)

            leftMin,leftMax = helper(root.left)
            rightMin,rightMax = helper(root.right)
            
            val = leftMax < root.val < rightMin
            
            if not val and self.res:
                self.res = val
                
            return (min(root.val,leftMin),max(root.val,rightMax))
        
        helper(root)
        
        return self.res
            
            


        
            
        
            
        
        
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
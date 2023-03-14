# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        self.nums = 0
        
        def backtrack(node,pfs,targetSum):
            
            if not node:
                return
            
            if not pfs:
                pfs.append(node.val)
                
            else:
                pfs.append(pfs[-1]+node.val)
                    
            if pfs[-1] == targetSum:
                self.nums += 1
                    
            for i in range(len(pfs)-1):
                if pfs[-1]-pfs[i] == targetSum:
                    self.nums += 1
                    
            backtrack(node.left,pfs[:],targetSum)
            backtrack(node.right,pfs[:],targetSum)
            
        backtrack(root,[],targetSum)
        return self.nums
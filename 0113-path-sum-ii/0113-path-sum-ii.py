# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.validNodesVals = []
        
        def backtrack(node,curSum,target,arr):
            
            if node and not node.left and not node.right:
                curSum += node.val
                arr.append(node.val)
                if curSum == target:
                    self.validNodesVals.append(arr)
                    
                return
                    
            if not node:
                return 
            
            curSum += node.val
            arr.append(node.val)
            backtrack(node.left,curSum,target,arr[:])
            backtrack(node.right,curSum,target,arr[:])
            
        backtrack(root,0,targetSum,[])
        return self.validNodesVals
        
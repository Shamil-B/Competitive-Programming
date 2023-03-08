# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        
        #return format (summ,nums,valids)
        
        def helper(root):
            if not root:
                return (0,0,0)
            
            valids = 0
            
            sumL,numsL,validsL = helper(root.left)
            sumR,numsR,validsR = helper(root.right)
            
            totalSum = sumL+sumR+root.val
            nums = numsL+numsR+1
            
            if nums!=0:
                ave = totalSum//nums
                if ave == root.val:
                    valids += 1
            
            valids += (validsL+validsR)
            
            
            return totalSum,nums,valids
        
        res = helper(root)
        return res[2]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        #find the depth first
        depth = 1
        stack = [(root,depth)]
        while stack:
            node,curDepth = stack.pop()
            
            if node.right:
                stack.append((node.right,curDepth+1))

            if node.left:
                stack.append((node.left,curDepth+1))
                
            if not node.right and not node.left:
                depth = max(depth,curDepth)
                
        #now sum the elements up on that level
        
        sum_ = 0
        stack = [(root,1)]
        while stack:
            node,curDepth = stack.pop()
            
            if node.right:
                stack.append((node.right,curDepth+1))

            if node.left:
                stack.append((node.left,curDepth+1))
                
            if curDepth == depth:
                sum_ += node.val
                
        return sum_
                
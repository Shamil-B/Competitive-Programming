# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        height = self.findHeight(root)

        if root and not root.right and not root.left:
            return [root.val]
        
        def helper(root,limit):
            if not root:
                return [],0,True
            
            curList = []
            if limit <= 0:
                curList.append(root.val)
                
            if root.right:
                tmpList,depth,once = helper(root.right,limit-1)
                curList += tmpList
                if root.left and once:
                    root.right = None
                    once = False

            else:
                tmpList,depth,once = helper(root.left,limit-1)
                curList += tmpList

            return curList,depth+1,once
        
        finalList = []
        limit = 0
        while root and (root.left or root.right):
            curList,curDepth,once = helper(root,limit)
            orig = finalList.copy()
            finalList += curList
            
            if curDepth >= height:
                break
            limit = max(limit,curDepth)
        return finalList
        
        
        
    def findHeight(self,root):
        if not root:
            return 0
        
        left = self.findHeight(root.left)
        right = self.findHeight(root.right)
        
        return 1+max(left,right)


            
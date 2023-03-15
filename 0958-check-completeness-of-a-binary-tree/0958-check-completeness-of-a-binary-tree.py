# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        
        self.heights = []
        self.lastLevel = []
        def backtrack(root,level):
            if not root:
                return 
            
            if root and (not root.left or not root.right):
                self.heights.append(level)
            
            backtrack(root.left,level+1)
            backtrack(root.right,level+1)
            
            
        backtrack(root,0)
        
        maxHeight = max(self.heights)
        count = 0
        for height in self.heights:
            if abs(height-maxHeight)>1:
                count += 1
                
        def lastLevel(root,level):
            if level == maxHeight:
                if root:
                    self.lastLevel.append(root.val)
                else:
                    self.lastLevel.append(root)
                    
            if not root:
                return

            lastLevel(root.left,level+1)
            lastLevel(root.right,level+1)
            
        lastLevel(root,0)
        print(self.heights,self.lastLevel)
        for i in range(len(self.lastLevel)-1):
            if self.lastLevel[i] == None and self.lastLevel[i+1] != None:
                return False
            
        return count == 0
            
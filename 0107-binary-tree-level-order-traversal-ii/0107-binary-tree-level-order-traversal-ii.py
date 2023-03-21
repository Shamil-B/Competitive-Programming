# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.levels = {}
        
        def traverseLevel(root,level):
            
            if not root:
                return 
            
            if level not in self.levels:
                self.levels[level] = [root.val]
                
            else:
                self.levels[level].append(root.val)
                
            traverseLevel(root.left,level+1)
            traverseLevel(root.right,level+1)

                
        traverseLevel(root,0)
        
        levels = list(self.levels.values())
        levels.reverse()
        return levels
                
                
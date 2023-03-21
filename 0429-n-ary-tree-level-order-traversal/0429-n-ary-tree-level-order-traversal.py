"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        self.levels = {}
        
        def levelTraversal(root,level):
            
            if not root:
                return
            
            if level not in self.levels:
                self.levels[level] = [root.val]
                
            else:
                self.levels[level].append(root.val)
                
            for child in root.children:
                levelTraversal(child,level+1)
                
        levelTraversal(root,0)
        return list(self.levels.values())
            
            
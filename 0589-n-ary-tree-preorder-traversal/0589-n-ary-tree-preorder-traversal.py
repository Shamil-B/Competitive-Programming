"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        self.nums = []
        def traversePre(node):
            
            if not node:
                return
            
            self.nums.append(node.val)
            
            for child in node.children:
                traversePre(child)
                
        traversePre(root)
        return self.nums
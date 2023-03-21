"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        self.vals = []
        def pot(node):
            if not node:
                return

            for child in node.children:
                pot(child)

            self.vals.append(node.val)
            
        pot(root)
        
        return self.vals
            
        

        
        
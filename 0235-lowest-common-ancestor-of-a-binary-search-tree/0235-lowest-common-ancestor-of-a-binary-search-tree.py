# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.lca = None
        def helper(root,p,q):
            
            if not root:
                return (False,False,None)
            
            pf = qf = False
            lca = None
            
            pfL,qfL,lcaL = helper(root.left,p,q)

            pfR,qfR,lcaR = helper(root.right,p,q)
            
            if root==p:
                pf = True
                
            if root==q:
                qf = True
                
            if (pfL or pfR or pf) and (qfL or qfR or qf) and not (lca or lcaL or lcaR) and not self.lca:
                lca = root
                self.lca = root
            
            return (pfL or pfR or pf),(qfL or qfR or qf),lca
            
        helper(root,p,q)
        return self.lca
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode],dic={},level=0) -> List[List[int]]:
        if not root:
            return []
        if level==0:
            dic = {level:[root.val]}
            
        else:
            ls = [] if not root else [root.val]
            if level not in dic:
                dic[level] = ls
         
            else:
                dic[level].append(ls[0])
                
        if root.left:
            self.levelOrder(root.left,dic,level+1)
            
        if root.right:
            self.levelOrder(root.right,dic,level+1)
        
        if level==0:
            return list(dic.values())
                
        
            
        
        
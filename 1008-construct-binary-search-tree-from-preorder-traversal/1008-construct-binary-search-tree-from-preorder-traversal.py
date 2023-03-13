# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        def buildBst(arr):
            node = TreeNode(arr[0])
            root = node
            
            for i in range(1,len(arr)):
                cur = root
                node = TreeNode(arr[i])
                while cur:
                    if cur.val>arr[i]:
                        prev1 = cur
                        cur = cur.left
                        
                        if not cur:
                            prev1.left = node
                    else:
                        prev2 = cur
                        cur = cur.right
                        if not cur:
                            prev2.right = node
                            
            return root
        
        return buildBst(preorder)
                        
                
            
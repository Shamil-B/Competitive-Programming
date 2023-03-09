# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.paths = []
        
        def backTrack(path,root):
            
            if root and not root.left and not root.right:
                if not path:
                    path += f"{root.val}"
                else:
                    path += "->"+f"{root.val}"

                self.paths.append(path[:])
                return
            
            if root:
                if not path:
                    path += f"{root.val}"
                else:
                    path += "->"+f"{root.val}"
                backTrack(path,root.left)
                backTrack(path,root.right)
                path = ""

        backTrack("",root)
        return self.paths
        
            
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        self.ans = []
        self.to_delete = set(to_delete)
        def solve(root, is_parent_dead):
            if not root:
                return False

            is_me_dead = root.val in self.to_delete
            left = solve(root.left, is_me_dead)
            right = solve(root.right, is_me_dead)
            
            if is_parent_dead and not is_me_dead:
                self.ans.append(root)
                
            if not is_me_dead:
                if left:
                    root.left = None
                if right:
                    root.right = None
                
            return is_me_dead
        
        solve(root, True)
        return self.ans
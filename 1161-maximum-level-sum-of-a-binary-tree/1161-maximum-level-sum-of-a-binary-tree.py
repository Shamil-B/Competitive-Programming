# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_ = -inf
        maxLevel = 1
        level = 0

        q = deque([root])
        visited = set()
        
        while q:            
            sum_ = 0
            level += 1
            for curNode in q:
                sum_ += curNode.val
                
            if sum_>max_:
                max_ = sum_
                maxLevel = level
            
            for i in range(len(q)):
                node = q.popleft()

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)
                    
        return maxLevel
            
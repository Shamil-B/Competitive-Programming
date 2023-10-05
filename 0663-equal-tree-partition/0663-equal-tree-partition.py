# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkEqualTree(self, root: Optional[TreeNode]) -> bool:
        def traverse(root):
            if not root:
                return 0

            val = root.val
            left = traverse(root.left)
            right = traverse(root.right)

            return val + left + right

        totalSum = traverse(root)
        def canPartition(root):
            nonlocal totalSum

            val = root.val
            leftSum = rightSum = 0
            isFoundLeft = isFoundRight = leftCheck = rightCheck = False

            if root.left:
                leftSum, isFoundLeft = canPartition(root.left)
                leftCheck = (leftSum == (totalSum / 2))

            if root.right:
                rightSum, isFoundRight = canPartition(root.right)
                rightCheck = (rightSum == (totalSum / 2))

            result = leftCheck or rightCheck

            answer = result or isFoundLeft or isFoundRight
            return val + leftSum + rightSum, answer
        
        
        bigAnswer = canPartition(root)[1]
        return bigAnswer
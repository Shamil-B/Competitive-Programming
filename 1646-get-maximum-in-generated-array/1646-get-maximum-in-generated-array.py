class Solution:
    def getMaximumGenerated(self, n):
        nums = [0]*(n+2)
        nums[1] = 1

        for curNum in range(2, n+1):
            nums[curNum] = nums[curNum//2] + nums[(curNum//2)+1] * (curNum%2)
    
        return max(nums[:n+1])
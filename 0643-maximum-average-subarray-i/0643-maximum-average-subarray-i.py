class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxSum = sum(nums[:k])
        curSum = 0
        
        p1 = p2 = 0
        
        while p2<len(nums):
            if p2==k:
                maxSum = curSum
                curSum = curSum -nums[p1] + nums[p2]
                maxSum = max(maxSum,curSum)
                
            elif p2>k:
                curSum = curSum -nums[p1] + nums[p2]
                maxSum = max(maxSum,curSum)
            else:
                curSum += nums[p2]
                p1-=1
                
            p2+=1
            p1+=1
            
        return maxSum/k
                
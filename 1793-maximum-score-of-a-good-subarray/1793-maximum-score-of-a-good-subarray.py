class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        
        
        size = 1
        leftInd = rightInd = k
        origSize = len(nums)
        maxScore = nums[k]
        min_ = nums[k]
        while (rightInd-leftInd+1) < origSize:
            left = right = 0
            if leftInd > 0:
                left = nums[leftInd-1]
                
            if rightInd < origSize-1:
                right = nums[rightInd+1]
                
            if left > right:
                leftInd -= 1
                min_ = min(min_,nums[leftInd])
                score = (rightInd-leftInd+1)*min_
                maxScore = max(maxScore,score)
                
                
            else:
                rightInd += 1      
                min_ = min(min_,nums[rightInd])
                score = (rightInd-leftInd+1)*min_
                maxScore = max(maxScore,score)
                
        return maxScore
            
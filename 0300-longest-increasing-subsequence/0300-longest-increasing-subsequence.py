class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        size = len(nums)
        @cache
        def solveTopDown(ind):
            max_ = 1
            for i in range(ind+1,size):
                if nums[ind] < nums[i]:
                    max_ = max(max_,solveTopDown(i)+1)

            return max_

        # max_ = 1
        # for i in range(size):
        #     max_ = max(max_,solveTopDown(i))
        # return max_

        def solveBottomUp():
            dp = [0]*size
            
            for i in range(size-1,-1,-1):
                for j in range(i-1,-1,-1):
                    if nums[j] < nums[i]:
                        dp[j] = max(dp[j],dp[i]+1)
                        
            return max(dp) +1
        
        return solveBottomUp()
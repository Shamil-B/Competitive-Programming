class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        for height in nums:
            left = bisect_left(dp, height)
            if left == len(dp): 
                dp.append(height)
            else: 
                dp[left] = height
        return len(dp)
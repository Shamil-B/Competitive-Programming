class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        for num in nums:
            left = bisect_left(dp, num)
            if left == len(dp): 
                dp.append(num)
            else: 
                dp[left] = num
        return len(dp)
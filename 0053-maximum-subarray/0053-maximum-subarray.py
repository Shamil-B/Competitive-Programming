class Solution:
    def maxSubArray(self, nums):
            max_sum_til_i = maxx= nums[0]
            for i, num in enumerate(nums[1:],start=1):
                max_sum_til_i = max(max_sum_til_i+num, num)
                maxx = max(maxx,max_sum_til_i)
            return maxx
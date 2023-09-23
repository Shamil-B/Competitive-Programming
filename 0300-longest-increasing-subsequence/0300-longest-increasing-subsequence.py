class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        size = len(nums)
        @cache
        def solve(ind):
            max_ = 1
            for i in range(ind+1,size):
                if nums[ind] < nums[i]:
                    max_ = max(max_,solve(i)+1)

            return max_

        max_ = 1
        for i in range(size):
            max_ = max(max_,solve(i))
        return max_
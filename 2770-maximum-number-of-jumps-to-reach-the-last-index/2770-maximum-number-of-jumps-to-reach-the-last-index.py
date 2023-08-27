class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        size = len(nums)

        @cache
        def solve(ind):
            if ind == size-1:
                return 0

            max_ = -1
            for i in range(ind+1,size):
                if abs(nums[i]-nums[ind]) <= target:
                    max_ = max(max_,solve(i))
 
            if max_ == -1:
                return -1
            return max_ + 1

        return solve(0)
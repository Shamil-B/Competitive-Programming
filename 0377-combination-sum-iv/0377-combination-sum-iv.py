class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        @cache
        def dp(sum_):
            if sum_ == target:
                return 1

            ways = 0
            for num in nums:
                if sum_+num>target:
                    break
                ways += dp(sum_ + num)

            return ways
        return dp(0)
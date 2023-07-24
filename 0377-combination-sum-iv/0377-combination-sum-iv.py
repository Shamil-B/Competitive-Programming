class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        self.ways = 0
        @cache
        def dp(sum_):
            if sum_ == target:
                return 1
            
            if sum_ > target:
                return 0
            
            ways = 0
            for num in nums:
                if sum_+num>target:
                    break
                ways += dp(sum_ + num)
            
            return ways
        ways = dp(0)
        return ways
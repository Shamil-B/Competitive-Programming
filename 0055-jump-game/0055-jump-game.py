class Solution:
    def canJump(self, nums: List[int]) -> bool:
        size = len(nums)

        @cache
        def solve(ind):
            if ind == size-1:
                return True

            for i in range(ind+1,min(size,ind+nums[ind]+1)):
                if solve(i):
                    return True

            return False
        
        return solve(0)
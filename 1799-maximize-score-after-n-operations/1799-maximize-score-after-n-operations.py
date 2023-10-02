class Solution:
    def maxScore(self, nums: List[int]) -> int:
        
        @cache
        def solve(n,nums):
            max_ = 0
            nums = list(nums)
            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i != j:
                        newNums = nums[:]
                        if i > j:
                            newNums.pop(i)
                            newNums.pop(j)
                        else:
                            newNums.pop(j)
                            newNums.pop(i)

                        max_ = max(max_, solve(n-1,tuple(newNums))+n*gcd(nums[i], nums[j]))
                        
            return max_

        return solve(len(nums)//2, tuple(nums[:]))
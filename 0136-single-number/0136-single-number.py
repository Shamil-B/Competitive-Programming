class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        sum1 = sum(list(set(nums)))
        sum2 = sum(nums)
        
        return sum1 - (sum2 - sum1)
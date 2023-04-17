class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x = 0
        y = 0

        for i in range(len(nums)):
            x = (x ^ nums[i]) & ~y
            y = (y ^ nums[i]) & ~x
        return x
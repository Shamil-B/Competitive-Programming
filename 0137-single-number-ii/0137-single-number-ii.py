class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return list(Counter(nums).keys())[list(Counter(nums).values()).index(1)]
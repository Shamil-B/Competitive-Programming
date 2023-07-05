class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_ = sum_ = 0
        for val in values:
            sum_ = max(sum_, max_ + val)
            max_ = max(max_, val) - 1
        return sum_
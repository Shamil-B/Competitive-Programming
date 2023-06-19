class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_ = -inf
        sum_ = 0
        for i in range(len(gain)):
            max_ = max(max_,sum_)
            sum_ += gain[i]
            
        return max(max_,sum_)
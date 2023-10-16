class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        min_ = min(nums)
        max_ = max(nums)
        mid = (min_+max_) // 2
        
        return (max_-min(max_-mid, k)) - (min_+min(mid-min_, k))
        
        
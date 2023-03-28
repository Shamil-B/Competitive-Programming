class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_ = max(nums)
        min_ = min(nums)
        count = 0
        ans = 0

        range_ = [0 for i in range(max_-min_+1)]
        for num in nums:
            range_[num-min_] += 1

        for i in range(len(range_)-1,-1,-1):
            if range_[i]>0:
                count += range_[i]
                if count>=k:
                    ans = i+min_
                    break
                
        return ans
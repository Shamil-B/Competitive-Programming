class Solution:
    def minSubArrayLen(self, target: int, nums) -> int:
        if sum(nums) < target:
            return 0
        
        left = right = 0
        n = len(nums)
        summ = 0
        minn = n
        while right < n+1:
            if summ < target:
                if right<n:
                    summ += nums[right]
                right += 1
                
            if summ >= target:
                minn = min(minn,right-left)
                summ -= nums[left]
                left += 1
                
        return minn
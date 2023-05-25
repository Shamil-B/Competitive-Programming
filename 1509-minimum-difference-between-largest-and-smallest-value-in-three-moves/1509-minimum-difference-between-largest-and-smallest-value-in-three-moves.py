class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums)<5:
            return 0

        minDiff = max(nums)-min(nums)


        #4 cases
        tmp = nums[:]
        # 0 3
        nums.remove(max(nums))
        nums.remove(max(nums))
        nums.remove(max(nums))
        if nums:
            minDiff = min(minDiff,max(nums)-min(nums))

        # 3 0
        nums = tmp[:]
        nums.remove(min(nums))
        nums.remove(min(nums))
        nums.remove(min(nums))
        if nums:
            minDiff = min(minDiff,max(nums)-min(nums))

        # 1 2
        nums = tmp[:]
        nums.remove(min(nums))
        nums.remove(max(nums))
        nums.remove(max(nums))
        if nums:
            minDiff = min(minDiff,max(nums)-min(nums))

        # 2 1
        nums = tmp[:]
        nums.remove(min(nums))
        nums.remove(min(nums))
        nums.remove(max(nums))
        if nums:
            minDiff = min(minDiff,max(nums)-min(nums))

        return minDiff
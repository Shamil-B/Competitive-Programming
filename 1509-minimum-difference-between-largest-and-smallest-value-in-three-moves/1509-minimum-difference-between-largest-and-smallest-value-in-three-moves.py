class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums)<5:
            return 0

        minDiff = max(nums)-min(nums)

        nums.sort()

        #4 cases

        # 0 3
        minDiff = min(minDiff,nums[-4]-nums[0])

        # 3 0
        minDiff = min(minDiff,nums[-1]-nums[3])


        # 1 2
        minDiff = min(minDiff,nums[-3]-nums[1])


        # 2 1
        minDiff = min(minDiff,nums[-2]-nums[2])


        return minDiff
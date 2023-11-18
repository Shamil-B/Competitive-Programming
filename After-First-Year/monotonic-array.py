class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        sorted_forward = True
        sorted_backward = True

        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                sorted_forward = False
                break

        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                sorted_backward = False
                break

        return sorted_forward or sorted_backward
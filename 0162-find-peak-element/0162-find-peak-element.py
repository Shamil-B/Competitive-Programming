class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        nums = [float("-inf")] + nums + [float("-inf")]
        low = -1
        high = n

        while low < high-1:
            mid = (low + high) // 2
            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid - 1

            elif nums[mid] < nums[mid+1]:
                # increasing
                low = mid

            else:
                # decreasing
                high = mid

        return low
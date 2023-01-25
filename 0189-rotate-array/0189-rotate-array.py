class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # for i in range(k):    #Solution 1
        #     nums.insert(0,nums.pop())

        k = k%len(nums)       #Solution 2
        new = nums[len(nums)-k:]+nums[:len(nums)-k]
        for i in range(len(new)):
            nums[i] = new[i]





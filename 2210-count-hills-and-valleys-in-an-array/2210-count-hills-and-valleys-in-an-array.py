class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        count = 0
        new_nums = []
        for i in range(len(nums)):
            if i == len(nums)-1 or nums[i] != nums[i+1]:
                new_nums.append(nums[i])
                
        print(new_nums)
        for i in range(1,len(new_nums)-1):
            if new_nums[i] > new_nums[i-1] and new_nums[i] > new_nums[i+1] or new_nums[i] < new_nums[i-1] and new_nums[i] < new_nums[i+1]:
                count += 1
        return count
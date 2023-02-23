class NumArray:
    
    def __init__(self, nums: List[int]):
        self.pfSum = nums
        
        for i in range(1,len(nums)):
            self.pfSum[i] = (self.pfSum[i] + self.pfSum[i-1])
        

    def sumRange(self, left: int, right: int) -> int:
        
        return (self.pfSum[right]-self.pfSum[left-1]) if left!=0 else self.pfSum[right]

#     def __init__(self, nums: List[int]):
#         self.nums = nums
#         self.pfSum = [nums[0]]
        
#         for i in range(1,len(nums)):
#             self.pfSum.append(self.nums[i] + self.pfSum[-1])
        

#     def sumRange(self, left: int, right: int) -> int:
        
#         return (self.pfSum[right]-self.pfSum[left-1]) if left!=0 else self.pfSum[right]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
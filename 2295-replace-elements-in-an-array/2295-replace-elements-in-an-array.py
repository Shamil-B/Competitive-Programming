class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        indices = {}
        
        for index, num in enumerate(nums):
            indices[num] = index
            
        for op in operations:
            index = indices[op[0]]
            num = op[1]
            
            nums[indices[op[0]]] = num
            indices[num] = index
            
        return nums
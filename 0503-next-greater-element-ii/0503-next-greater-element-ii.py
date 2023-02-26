class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        res = []
        dic = {}
        nums = nums*2
        
        for i in range(len(nums)):
            while stack and nums[i] > nums[stack[-1]]:
                dic[stack.pop()] = nums[i]
                
            stack.append(i)
            
        for i in range(len(nums)//2):
            if i in dic:
                res.append(dic[i])
                
            else:
                res.append(-1)
                
        return res
            
    
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        maxx = len(nums)+1
        dic = {}
        
        for num in nums:
            dic[num] = 1
        
        for i in range(maxx):
            if i not in dic:
                return i
            
            
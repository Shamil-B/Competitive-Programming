class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        dic = {}
        maxx = max(nums)
        
        for num in nums:
            if num > 0:
                dic[num] = 0
                
                
        for i in range(1,maxx+1):
            if i not in dic:
                return i
            
        if maxx+1 > 0:
            return maxx+1
        
        return 1
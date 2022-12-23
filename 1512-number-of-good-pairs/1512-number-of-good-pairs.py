class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        
        for i in range(n):
            for j in range(n):
                if nums[i]==nums[j] and i<j:
                    count+=1
                    
        return count
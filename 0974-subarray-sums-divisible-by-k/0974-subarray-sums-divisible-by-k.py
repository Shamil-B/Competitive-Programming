class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        subArrays = 0
        dic = {0:1}
        
        n = len(nums)
        
        for i in range(1,n):
            nums[i] += nums[i-1]
            
            
        for num in nums:
            rem = num%k
            if rem in dic:
                subArrays += dic[rem]
                dic[rem] += 1
                
            else:
                dic[rem] = 1
                
        return subArrays
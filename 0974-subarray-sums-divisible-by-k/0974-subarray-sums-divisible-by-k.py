class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        subArrays = 0
        dic = {0:1}
        
        pfs = [nums[0]]
        n = len(nums)
        
        for i in range(1,n):
            pfs.append(pfs[i-1]+nums[i])
            
            
        for num in pfs:
            rem = num%k
            if rem in dic:
                subArrays += dic[rem]
                dic[rem] += 1
                
            else:
                dic[rem] = 1
                
        return subArrays
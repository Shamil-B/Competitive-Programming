class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        pfsDic = {0:1}
        
        pfs = [nums[0]]
        n = len(nums)
        for i in range(1,n):
            pfs.append(pfs[i-1]+nums[i])
            
        count = 0
        for num in pfs:
            if (num-goal) in pfsDic:
                count += pfsDic[num-goal]
                
            if num in pfsDic:
                pfsDic[num] += 1
                
            else:
                pfsDic[num] = 1
                
        return count
                
        
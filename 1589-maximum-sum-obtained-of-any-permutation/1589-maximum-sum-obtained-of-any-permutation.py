class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        pfs = [0]*n
        
        for r in requests:
            pfs[r[0]] += 1
            if r[1] < n-1:
                pfs[r[1]+1] -= 1
                
        for i in range(1,n):
            pfs[i] += pfs[i-1]
            
        pfs.sort()
        nums.sort()
        totalSum = 0

        for i in range(n):
            totalSum += (nums[i]*pfs[i])
            
        return totalSum%(10**9+7)
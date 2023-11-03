class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        pfs = [nums[0]]
        rpfs = [nums[-1]]
        n = len(nums)
        for i in range(1, n):
            pfs.append(nums[i]+pfs[-1])
        for i in range(len(nums)-2,-1,-1):
            rpfs.append(nums[i]+rpfs[-1])
            
        count = 0
        print(pfs,rpfs)
        for i in range(n-1):
            if pfs[i] >= rpfs[n-i-2]:
                count += 1
        return count
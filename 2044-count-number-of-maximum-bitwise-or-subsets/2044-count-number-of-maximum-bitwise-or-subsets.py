class Solution:
    def countMaxOrSubsets(self, nums) -> int:
        maxOr = 0
        subsets = 0
        n = len(nums)
        for num in nums:
            maxOr |= num
        
        def backtrack(path,ind):
            nonlocal subsets,maxOr

            if path==maxOr:
                subsets += 1
                
            if ind==n:
                return

            for i in range(ind,len(nums)):
                    tmp = path
                    path |= nums[i]

                    backtrack(path,i+1)
                    
                    path = tmp

        backtrack(0,0)
        return subsets
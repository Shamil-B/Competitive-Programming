class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        n = len(nums)
        setWithBits = 0
        def backtrack(path,ind):
            nonlocal subsets,n,setWithBits
            
            subsets.append(path[:])

            for i in range(ind,n):
                if (1<<i & setWithBits)==0:
                    path.append(nums[i])
                    setWithBits |= 1<<i 
                    
                    backtrack(path,i+1)

                    path.pop()
                    setWithBits ^= 1<<i
                    
        backtrack([],0)
        return subsets
            
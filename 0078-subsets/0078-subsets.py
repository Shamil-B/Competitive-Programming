class Solution:
    def subsets(self, nums):
        
        self.finalArr = []
        self.nums = nums

        def backtrack(container,candidate):
            
            self.finalArr.append(container[:])
            
            candidates = [i for i in range(candidate,len(self.nums))]

            for candidate in candidates:
                container.append(self.nums[candidate])
                backtrack(container,candidate+1)
                container.pop()
            
        backtrack([],0)

        return self.finalArr
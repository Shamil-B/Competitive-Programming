class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        
        self.subSeqs = []
        self.unique = set()
        def backtrack(path,nums):
            
            if len(path)>1 and tuple(path) not in self.unique:
                self.subSeqs.append(path)
                self.unique.add(tuple(path))
            
            for i in range(len(nums)):
                if not path or path[-1] <= nums[i]:
                    path.append(nums[i])
                    backtrack(path[:],nums[i+1:])
                    path.pop()
                    
        backtrack([],nums)
        return self.subSeqs
                    
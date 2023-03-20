class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        
        self.subSeqs = []
        self.unique = set()
        def backtrack(path,ind):
            
            if len(path)>1:
                tp = tuple(path)
                if tp not in self.unique:
                    self.subSeqs.append(path)
                    self.unique.add(tp)
            
            for i in range(ind,len(nums)):
                if not path or path[-1] <= nums[i]:
                    path.append(nums[i])
                    backtrack(path[:],i+1)
                    path.pop()
                    
        backtrack([],0)
        return self.subSeqs
                    
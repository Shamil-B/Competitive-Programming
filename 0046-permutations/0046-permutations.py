class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.permutations = []
        n = len(nums)
        sett = set()
        candidates = [nums[i] for i in range(n)]
        def backtrack(path):
            
            if len(path)==n:
                self.permutations.append(path[:])
                return
            
            for c in candidates:
                if c not in sett:
                    path.append(c)
                    sett.add(c)
                    backtrack(path[:])
                    sett.remove(path.pop())
        
        backtrack([])
        return self.permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.permutations = []
        n = len(nums)
        setWithBit = 0
        candidates = [nums[i] for i in range(n)]
        self.num = 2**n-1
        def backtrack(path):
            nonlocal setWithBit
            if self.num==setWithBit:
                self.permutations.append(path[:])
                return

            for i in range(n):
                if 1<<i&setWithBit==0:
                    path.append(candidates[i-1])
                    setWithBit |= 1<<i
                    backtrack(path[:])
                    path.pop()
                    setWithBit ^= 1<<i
        
        backtrack([])
        return self.permutations
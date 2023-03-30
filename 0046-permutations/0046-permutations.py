class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        n = len(nums)
        setWithBit = 0
        candidates = [nums[i] for i in range(n)]
        target = 2**n-1
        path = []
        def backtrack():
            nonlocal setWithBit,target,permutations,path

            if target == setWithBit:
                permutations.append(path[:])
                return

            for i in range(n):
                if 1<<i&setWithBit==0:
                    path.append(candidates[i-1])
                    setWithBit |= 1<<i

                    backtrack()

                    path.pop()
                    setWithBit ^= 1<<i
        
        backtrack()
        return permutations
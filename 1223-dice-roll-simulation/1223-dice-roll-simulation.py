class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        
        @cache
        def solve(roll,last,freq):
            if roll > n:
                return 1

            ways = 0
            for i in range(1,7):
                if i == last:
                    if freq < rollMax[i-1]:
                        ways += solve(roll+1,last,freq+1)

                else:
                    ways += solve(roll+1,i,1)

            return ways
        
        return solve(1,-1,0)%(pow(10,9)+7)
            
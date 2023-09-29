class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        size = len(satisfaction)
        satisfaction.sort()

        @cache
        def solve(ind, time):
            if ind >= size:
                return 0
            
            likeTimeCoeficient = time * satisfaction[ind]

            pick = solve(ind+1, time + 1) + likeTimeCoeficient
            skip = solve(ind+1,time)
            
            return max(pick, skip)
        
        return solve(0,1)

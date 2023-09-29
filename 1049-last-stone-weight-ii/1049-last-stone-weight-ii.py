class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stones = [0] + stones
        stones.sort()

        @cache
        def solve(ind,sum_):
            if ind >= len(stones):
                return abs(sum_)

            plus = solve(ind+1,sum_+stones[ind])
            minus = solve(ind+1,sum_-stones[ind]) 
            return min(plus,minus)

        return solve(0,0)
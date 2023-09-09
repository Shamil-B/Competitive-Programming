class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:   
        @cache
        def solve(start,end):
            cost = inf
            for cut in cuts:
                if cut < end and cut > start:
                    cost = min(cost,solve(start,cut)+solve(cut,end)+(end-start))
 
            if cost == inf:
                return 0
            return cost

        return solve(0,n)
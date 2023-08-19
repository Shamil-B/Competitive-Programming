class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        @cache
        def solve(ind,passes):
            if ind >= len(days):
                return 0
            
            if passes < 0:
                return inf
            
            if ind>0:
                passes -= (days[ind]-days[ind-1])
            
            if passes > 0:
                return solve(ind+1,passes)
            
            else:
                oneDay = solve(ind+1,1) + costs[0]
                sevenDay = solve(ind+1,7) + costs[1]
                thirtyDay = solve(ind+1,30) + costs[2]
                return min(oneDay,sevenDay,thirtyDay)
            
        return solve(0,0)
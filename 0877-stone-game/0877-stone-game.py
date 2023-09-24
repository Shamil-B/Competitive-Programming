class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        @cache
        def solve(l,r,isAlice):
            if l >= r:
                return 0

            if isAlice:
                return max(solve(l+1,r,not isAlice) + piles[l],solve(l,r-1,not isAlice) + piles[r])

            else:
                return min(solve(l+1,r,not isAlice) + piles[l],solve(l,r-1,not isAlice) + piles[r])

        
        res = solve(0,len(piles)-1,True)
        return res > (sum(piles)-res)
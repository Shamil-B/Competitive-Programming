class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        self.found = False
        coins.sort(reverse=True)

        @cache
        def solve(ind,amount):
            if amount < 0:
                return inf

            if amount == 0:
                self.found = True
                return 0
            
            min_ = inf
            for i in range(len(coins)):
                res = solve(i,amount-coins[i])
                min_ = min(min_,res)
                
            return min_+1
        
        ans = solve(0,amount)
        if not self.found:
            return -1
        return ans
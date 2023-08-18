class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def solve(day,have_stock,memo,stocks):
            if day >= len(prices):
                return 0
            
            state = (day,have_stock,stocks)
            if state in memo:
                return memo[state]
            
            if have_stock and stocks == 2:
                res = max(prices[day],solve(day+1,True,memo,stocks))
                memo[state] = res
                return memo[state]
            
            elif have_stock:
                sell = solve(day+1,False,memo,stocks) + prices[day]
                avoid = solve(day+1,True,memo,stocks)
                res = max(sell,avoid)
                memo[state] = res
                return memo[state]

            else:
                buy = solve(day+1,True,memo,stocks+1)-prices[day]
                avoid = solve(day+1,False,memo,stocks)
                res = max(buy,avoid)
                memo[state] = res
                return memo[state]
        memo = {}
        return solve(0,False,memo,0)
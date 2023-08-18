class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def solve(day,have_stock):
            if day >= len(prices):
                return 0

            if have_stock:
                sell = solve(day+1,False)+prices[day]
                avoid = solve(day+1,True)
                return max(sell,avoid)
            else:
                buy = solve(day+1,True)- prices[day]
                avoid = solve(day+1,False)
                return max(buy,avoid)
            
        return solve(0,False)
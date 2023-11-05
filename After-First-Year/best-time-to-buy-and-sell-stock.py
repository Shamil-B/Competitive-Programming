class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def solve(day,have_stock,memo):
            if day >= len(prices):
                return 0
            
            state = (day,have_stock)
            if state in memo:
                return memo[state]
            
            if have_stock:
                res = max(prices[day],solve(day+1,True,memo))
                memo[state] = res
                return memo[state]

            else:
                buy = solve(day+1,True,memo)-prices[day]
                avoid = solve(day+1,False,memo)
                res = max(buy,avoid)
                memo[state] = res
                return memo[state]
        memo = {}
        return solve(0,False,memo)

#         def solve(day,have_stock):
#             if day >= len(prices):
#                 return 0

#             if have_stock:
#                 sell = solve(day+1,False)+prices[day]
#                 avoid = solve(day+1,True)
#                 return max(sell,avoid)
#             else:
#                 buy = solve(day+1,True)- prices[day]
#                 avoid = solve(day+1,False)
#                 return max(buy,avoid)
            
#         return solve(0,False)
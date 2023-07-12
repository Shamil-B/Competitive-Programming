class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # if u haven't bought
        # choices are (buy) or (skip)
        # if u have bought
        # choices are (sell and jump) or (skip) 
        def solve(index,bought):

            if index >= len(prices):
                return 0

            state = (index,bought)
            if state not in memo:
                if bought == -1:
                    memo[state] = max(solve(index+1,bought),solve(index+1,prices[index]))
                else:
                    memo[state] =  max(solve(index+1,bought),solve(index+2,-1)+prices[index]-bought)

            return memo[state]

        memo = {}
        return solve(0,-1)
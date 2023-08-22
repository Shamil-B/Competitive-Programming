class Solution:
    def countVowelStrings(self, n: int) -> int:
        
        vowels = ["a","e","i","o","u"]
        # @lru_cache(None)
        def solve(ind,size):

            if ind > 4 or size >= n:
                return 1

            state = (ind,size)
            if state not in memo:
                ways = 0
                for i in range(ind,5):
                    ways += solve(i,size+1)
                
                memo[state] = ways
            return memo[state]

        memo = {}
        return solve(0,0)
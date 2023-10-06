class Solution:
    def integerBreak(self, n: int) -> int:
        
        @cache
        def solve(num, steps):
            if num == 0 and steps == 1:
                return 0

            if num == 1 or num == 0:
                return 1

            if num < 0:
                return 0

            max_ = 0
            for i in range(num, 0, -1):
                max_ = max(max_, solve(num-i, steps+1)*i)

            return max_

        return solve(n, 0)
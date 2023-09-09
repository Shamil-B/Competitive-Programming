class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        @cache
        def solve(curNum,sum_):
            if sum_ == n:
                return 1

            if sum_ > n or sum_ + pow(curNum,x) > n:
                return 0

            return solve(curNum+1,sum_+pow(curNum,x)) + solve(curNum+1,sum_)
        return solve(1,0) % (pow(10,9)+7)
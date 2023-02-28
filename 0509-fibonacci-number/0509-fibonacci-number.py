class Solution:
    def fib(self, n: int,memo={}) -> int:
        if n == 1 or n == 0:
                return n

        if n in memo:
            return memo[n]

        memo[n] = self.fib(n-1,memo) + self.fib(n-2,memo)

        return memo[n]

    
#     def fib(self, n: int) -> int:
#         if n == 1 or n == 0:
#             return n
        
#         return self.fib(n-1) + self.fib(n-2)
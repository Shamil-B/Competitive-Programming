class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = (pow(10, 9) + 7)
        def power(num, exponent, k):
            num = num % k
            product = 1
            while exponent > 0:
                if exponent%2 == 1:
                    product = (product*num)%k
                num = (num*num)%k
                exponent //= 2
            return product

        if n%2:
            ans = power(5, n//2+1, MOD) * power(4, n//2, MOD)
        else:
            ans = power(5, n//2, MOD) * power(4, n//2, MOD)

        return ans % MOD
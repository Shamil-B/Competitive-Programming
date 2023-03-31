class Solution:
    def countPrimes(self, n: int) -> int:
        if n<2:
            return 0

        isPrime = [True for i in range(n)]
        isPrime[0] = isPrime[1] = False
        
        i = 2
        count = 0
        while i*i<=n:
            if isPrime[i]:
                j = i*i
                while j<n:
                    isPrime[j] = False
                    j += i            
            
            i += 1
        
        for num in isPrime:
            if num:
                count += 1

        return count
        
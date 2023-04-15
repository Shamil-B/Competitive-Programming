class Solution:
    def closestPrimes(self, left: int, right: int) -> list[int]:
        sieve = [False] * (right+1)
        
        lastPrime = -1
        result = [-1, -1]
        for p in range(2, right+1):
            if not sieve[p]:
                for p2 in range(p*2, right+1, p):
                    sieve[p2] = True
                if left <= p <= right:
                    if lastPrime == -1:
                        lastPrime = p
                    elif result == [-1, -1]:
                        result = [lastPrime, p]
                    elif p - lastPrime < result[1] - result[0]:
                        result = [lastPrime, p]
                    lastPrime = p

        return result
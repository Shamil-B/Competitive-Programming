class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        bigSet = set()
        
        for num in nums:
            res = self.primeFacSet(num)
            bigSet = bigSet.union(res)

        return len(bigSet)

    def primeFacSet(self,num):
        disPrimes = set()
        d = 2
        while d<=num:
            while num%d==0:
                if d not in disPrimes:
                    disPrimes.add(d)
                num //= d
            d += 1
            
        return disPrimes
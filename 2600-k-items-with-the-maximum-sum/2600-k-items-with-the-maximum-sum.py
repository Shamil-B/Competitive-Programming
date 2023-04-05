class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        if k<=numOnes:
            return k
        
        summ = numOnes
        k -= numOnes
        k -= numZeros
        if k>0:
            summ += -1*(k)
        return summ
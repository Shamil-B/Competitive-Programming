class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        arr = [1 for i in range(numOnes)] + [0 for i in range(numZeros)] + [-1 for i in range(numNegOnes)]
        
        return sum(arr[:k])
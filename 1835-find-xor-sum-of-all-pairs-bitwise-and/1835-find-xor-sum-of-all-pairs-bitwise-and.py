class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        ans = 0
        size1 = len(arr1)
        size2 = len(arr2)

        xorSum1 = 0
        for i in range(size1):
            xorSum1 ^= arr1[i]
            
        xorSum2 = 0
        for i in range(size2):
            xorSum2 ^= arr2[i]
            
        return xorSum1 & xorSum2
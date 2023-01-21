class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        result = 0 
        piles.sort()
        for i in range(len(piles)-2,(len(piles)//3)-1,-2):
            piles.pop()
            result += piles.pop()
            piles.pop(0)
            if len(piles)==0:
                return result
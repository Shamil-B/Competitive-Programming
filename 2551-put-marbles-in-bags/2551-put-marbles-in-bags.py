class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        dividers = []
        n = len(weights)
        
        for i in range(n-1):
            dividers.append(weights[i] + weights[i+1])
        
        dividers.sort()
        return sum(dividers[n-k:]) - sum(dividers[:k-1])
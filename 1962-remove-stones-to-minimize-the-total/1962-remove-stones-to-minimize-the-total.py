class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        for index,pile in enumerate(piles):
            piles[index] = -1*pile

        heapq.heapify(piles)
        sum_ = 0
        while k:
            value = heapq.heappop(piles)
            value = abs(value)
            
            value -= (value // 2)
            heapq.heappush(piles,-1*value)
            k -= 1
            
        return sum(piles)*(-1)

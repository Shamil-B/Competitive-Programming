class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while True:
            stones = sorted(stones,reverse = True)

            if len(stones) == 1:
                return stones[0]

            elif len(stones) == 0:
                return 0

            y = stones.pop(0)
            x = stones.pop(0)

            if y == x:
                continue
            else:
                stones.append(y-x)
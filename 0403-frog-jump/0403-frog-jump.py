class Solution:
    def canCross(self, stones: List[int]) -> bool:
        stonesIndex  = {}
        
        for index, stone in enumerate(stones):
            stonesIndex[stone] = index

        size = len(stones)
        @cache
        def solve(curStone, unit):
            if curStone not in stonesIndex:
                return False
            
            if stonesIndex[curStone] == size-1:
                return True
            
            # k-1, k, k+1
            if unit <= 1:
                choiceOne = False

            else:
                choiceOne = solve(curStone + unit-1,unit-1)
                
            choiceTwo = solve(curStone + unit,unit)
            choiceThree = solve(curStone + unit+1,unit+1)

            return choiceOne or choiceTwo or choiceThree
        
        return solve(stones[0]+1,1)
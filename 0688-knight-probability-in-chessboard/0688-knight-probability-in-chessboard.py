class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        def solve(cord,k):
            if self.checkCord(cord,n) == 0 or k < 0:
                return 0

            valids = 0
            nextMoves = [(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1)]
            state = (cord,k)
            if state not in memo:
                for move in nextMoves:
                    valids += solve((cord[0]+move[0],cord[1]+move[1]),k-1)
                    
                
                memo[state] = valids + (1 if k == 0 else 0)
                
            return memo[state]
            
        memo = {}
        res = solve((row,column),k)
        return res/(8**k)
            
    def checkCord(self,cord,n):
        if cord[0] < 0 or cord[1] < 0 or cord[0] > n-1 or cord[1] > n-1:
            return 0
        
        return 1
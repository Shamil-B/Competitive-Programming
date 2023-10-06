class Solution:
    def knightDialer(self, n: int) -> int:
        dialer = []
        i = 1
        rows = 4
        cols = 3
        for row in range(3):
            curRow = []
            for col in range(3):
                curRow.append(i)
                i += 1
            dialer.append(str(curRow))

        dialer.append(["*","0","#"])

        cache
        def getPositions(cord):
            row, col = cord
            positions = []
            # up left
            if row-2 >= 0 and col-1 >= 0:
                positions.append((row-2,col-1))
                
            # up right
            if row-2 >= 0 and col+1 < cols:
                positions.append((row-2,col+1))
                
            # down left
            if row+2 < rows and col-1 >= 0:
                positions.append((row+2,col-1))
                
            # down right
            if row+2 < rows and col+1 < cols:
                positions.append((row+2,col+1))
                
            # left up
            if row-1 >= 0 and col-2 >= 0:
                positions.append((row-1,col-2))
                
            # left down
            if row+1 < rows and col-2 >= 0:
                positions.append((row+1,col-2))
                
            # right up
            if row-1 >= 0 and col+2 < cols:
                positions.append((row-1,col+2))
                
            # right down
            if row+1 < rows and col+2 < cols:
                positions.append((row+1,col+2))
                
            return positions
            
        @cache
        def solve(cord, size):
            row, col = cord

            if dialer[row][col] == "*" or dialer[row][col] == "#":
                return 0
            
            if size == n:
                return 1

            ways = 0
            for pos in getPositions(cord):
                ways += solve(pos, size+1)

            return ways

        ways = 0
        for row in range(3):
            for col in range(3):
                res = solve((row, col), 1)
                ways += res
                
        ways += solve((3, 1), 1)
        return ways % (pow(10, 9) + 7)
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.found = []
        
        def solve(row,uCol = None,uSlope = None):
            if not uCol:
                uCol = []
                
            if not uSlope:
                uSlope = []

            if row >= n:
                self.found.append(uCol[:])
                return

            for i in range(n):
                if i not in uCol and (row,i) not in uSlope:
                    newCol = uCol[:]
                    newCol.append(i)
                    newSlope = uSlope[:]

                    for j in range(i+1,n):
                        newSlope.append((row+(j-i),j))

                    for j in range(i-1,-1,-1):
                        newSlope.append((row+(i-1-j+1),j))

                    solve(row+1,newCol,newSlope)
        solve(0)
        ans = []
        for row in range(len(self.found)):
            grid = []
            for i in range(n):
                term = ""
                for j in range(n):
                    if self.found[row][i] == j:
                        term += "Q"

                    else:
                        term += "."
                        
                grid.append(term)
                
            ans.append(grid)

        return ans
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:

        self.board = board
        visited = set()
        q = deque([click])
        while q:
            row, col = q.popleft()
            cord = (row,col)

            if board[row][col] == 'M':
                board[row][col] = "X"
                break

            adjMines = self.checkAdj(cord)

            if adjMines > 0:
                board[row][col] = str(adjMines)

            else:
                neighbours = self.getNeighbours(cord)
                board[row][col] = "B"
                for neig in neighbours:
                    if neig not in visited:
                        visited.add(neig)
                        q.append(neig)
                    
        return board
    
    def checkAdj(self,cord):
        mines = 0
        row, col = cord
        
        if row < 0 or col < 0 or row >= len(self.board) or col >= len(self.board[0]):
            return 0

        if row>0 and col>0 and self.board[row-1][col-1] == "M":
            mines += 1

        if row>0 and self.board[row-1][col] == "M":
            mines += 1
            
        if col>0 and self.board[row][col-1] == "M":
            mines += 1
            
        if row<len(self.board)-1 and col<len(self.board[0])-1 and self.board[row+1][col+1] == "M":
            mines += 1
            
        if row<len(self.board)-1 and self.board[row+1][col] == "M":
            mines += 1
            
        if col<len(self.board[0])-1 and self.board[row][col+1] == "M":
            mines += 1
            
        if row>0 and col<len(self.board[0])-1 and self.board[row-1][col+1] == "M":
            mines += 1
            
        if row<len(self.board)-1 and col>0 and self.board[row+1][col-1] == "M":
            mines += 1
            
        return mines
    
    def getNeighbours(self,cord):
        neighs = []
        row, col = cord

        if row < 0 or col < 0 or row >= len(self.board) or col >= len(self.board[0]):
            return []

        if row>0 and col>0:
            neighs.append((row-1,col-1))
            
        if row>0:
            neighs.append((row-1,col))
            
        if col>0:
            neighs.append((row,col-1))
            
        if row<len(self.board)-1 and col<len(self.board[0])-1:
            neighs.append((row+1,col+1))
            
        if row<len(self.board)-1:
            neighs.append((row+1,col))
            
        if col<len(self.board[0])-1:
            neighs.append((row,col+1))
            
        if row>0 and col<len(self.board[0])-1:
            neighs.append((row-1,col+1))
            
        if row<len(self.board)-1 and col>0:
            neighs.append((row+1,col-1))
            
        return neighs


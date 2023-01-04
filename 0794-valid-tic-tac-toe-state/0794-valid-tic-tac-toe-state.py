class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        
        #There are 4 cases for failure of the game
        
        #First go through the grid and count number of X, O and wins
        
        numX = xwins = owins = numO = 0
      
        for row in range(3):
            for col in range(3):
                if board[row][col] == 'X':
                    numX += 1
                    
                elif board[row][col] == 'O':
                    numO += 1
                    
                    
                  
        #horizontal and vertical wins counting
        
        for row in range(3):
            
            if board[row][0] == 'X' and board[row][0] == board[row][1] and board[row][1] == board[row][2]:
                xwins += 1
                
            if board[0][row] == 'X' and board[0][row] == board[1][row] and board[1][row] == board[2][row]:
                xwins += 1
                
            if board[row][0] == 'O' and board[row][0] == board[row][1] and board[row][1] == board[row][2]:
                owins += 1
                
            if board[0][row] == 'O' and board[0][row] == board[1][row] and board[1][row] == board[2][row]:
                owins += 1
                
        
        
        #diagonal wins counting
        
        if board[0][0] == 'X' and board[0][0] == board[1][1] and board[0][0] == board[2][2]:
            xwins += 1
            
        if board[0][2] == 'X' and board[0][2] == board[1][1] and board[0][0] == board[2][0]:
            xwins += 1
            
        if board[0][0] == 'O' and board[0][0] == board[1][1] and board[0][0] == board[2][2]:
            owins += 1
            
        if board[0][2] == 'O' and board[0][2] == board[1][1] and board[0][2] == board[2][0]:
            owins += 1
            
        # first case
        
        if numX == 0 and numO==1:
            return False
        
        # second case
        if (numX > numO + 1) or (numO > numX):
            return False
        
        # third case
        
        if xwins+owins > 1 and (numX + numO < 9):
            return False
        
        if xwins == 1 and (numX <= numO):
            return False
        
        if owins > 0 and numX != numO:
            return False
        

        return True
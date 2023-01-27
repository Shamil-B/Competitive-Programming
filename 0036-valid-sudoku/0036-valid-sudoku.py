class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxes = [{} for i in range(9)]
        
        #check one row wise
        for row in board:
            
            dic = {}
            for num in row:

                if num in dic:
                    return False
                
                elif num != '.':
                    dic[num] = 0
                
                
        #check two column wise

                    
        for col in range(9):
            
            dic = {}
            for row in range(9):
                num = board[row][col]
                
                if num in dic:
                    return False
                
                elif num != '.':
                    dic[num] = 0
                    
                    ind = row - row%3
                    ind = ind + col//3
                    
                    
                    if num in boxes[ind]:
                        return False
                    
                    else:
                        boxes[ind][num] = 0
                            
        return True
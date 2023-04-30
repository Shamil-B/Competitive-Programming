class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows = len(maze)
        cols = len(maze[0])

        entrance = tuple(entrance)
        level = 0
        q = deque([(entrance,level)])
        
        visited = set()
        
        while q:
            curPos,level = q.popleft()
            
            row,col = curPos

            if (row==0 or row==rows-1 or col==0 or col==cols-1) and curPos!=entrance:
                return level

            if curPos in visited:
                continue
                
            visited.add(curPos)
            

            #up
            if row>0:
                if maze[row-1][col]=='.':
                    q.append(((row-1,col),level+1))
            #down
            if row<rows-1:
                if maze[row+1][col]=='.':
                    q.append(((row+1,col),level+1))

            #left
            if col>0:
                if maze[row][col-1]=='.':
                    q.append(((row,col-1),level+1))

            #right
            if col<cols-1:
                if maze[row][col+1]=='.':
                    q.append(((row,col+1),level+1))
                    
                    
        return -1

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        shortcut = {}
        n = len(board)
        for i in range(n):
            for j in range(n):
                if board[i][j] != -1:
                    row = n-1-i
                    if row % 2:
                        col = n-1-j+1
                    else:
                        col = j+1

                    num = row*n + col
                    shortcut[num] = board[i][j] 
                    
        q = [(0,1,False)]
        heapq.heapify(q)
        visited = set()

        while q:
            level, cur, tookRide = heapq.heappop(q)

            if cur >= n**2:
                return level
            
            
            if cur in shortcut and not tookRide:
                heapq.heappush(q,(level, shortcut[cur],True))
   
            else:
                if cur not in visited:                
                    visited.add(cur)

                    for i in range(1,7):
                        heapq.heappush(q,(level+1, cur+i,False))
        return -1
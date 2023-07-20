class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # we will use bfs to try every possiblity until target
        targetState = [[1,2,3],[4,5,0]]
        q = deque([(board[:],0)])
        visited = set()
        while q:
            curState, level = q.popleft()
            if curState == targetState:
                return level
            
            state = ""
            emp = (0,0)
            for i in range(2):
                for j in range(3):
                    if curState[i][j] == 0:
                        emp = (i,j)
                    state += str(curState[i][j])

            if state in visited:
                continue

            visited.add(state)
            row, col = emp

            if row == 1 or row == 0:
                tmp = copy.deepcopy(curState)
                tmp[1][col], tmp[0][col] = tmp[0][col], tmp[1][col]
                q.append((tmp,level+1))

            if col > 0:
                tmp = copy.deepcopy(curState)
                tmp[row][col-1], tmp[row][col] = tmp[row][col], tmp[row][col-1]
                q.append((tmp,level+1))

            if col < 2:
                tmp = copy.deepcopy(curState)
                tmp[row][col+1], tmp[row][col] = tmp[row][col], tmp[row][col+1]
                q.append((tmp,level+1))
                
        return -1
            
            
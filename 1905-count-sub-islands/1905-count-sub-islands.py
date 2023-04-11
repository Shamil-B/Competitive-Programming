class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        
        def dfs(cord):
            
            visited = set()
            stack = [cord]
            
            while stack:
                node = stack.pop()
                if node in visited:
                    continue
                
                x = node[0]
                y = node[1]
                visited.add(node)
                self.explored.add(node)

                if x>0 and grid2[x-1][y]:
                    if grid1[x-1][y]==0:
                        return False

                    else:
                        stack.append((x-1,y))
                        
                if y>0 and grid2[x][y-1]:
                    if grid1[x][y-1]==0:
                        return False

                    else:
                        stack.append((x,y-1))

                if x<len(grid2)-1 and grid2[x+1][y]:
                    if grid1[x+1][y]==0:
                        return False

                    else:
                        stack.append((x+1,y))

                if y<len(grid2[0])-1 and grid2[x][y+1]:
                    if grid1[x][y+1]==0:
                        return False

                    else:
                        stack.append((x,y+1))

            return True

        self.explored = set()
        subIslands = 0

        for row in range(len(grid1)):
            for col in range(len(grid1[0])):
                if grid2[row][col] and ((row,col) not in self.explored) and grid1[row][col]:
                    if dfs((row,col)):
                        subIslands += 1

        return subIslands
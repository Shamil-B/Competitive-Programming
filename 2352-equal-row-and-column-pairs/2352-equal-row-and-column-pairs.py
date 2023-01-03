class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        dic = {}
        count = 0
        
        for row in grid:
            row = tuple(row)
            
            if row not in dic:
                dic[row] = 1
                
            else:
                dic[row] += 1
                
        grid2 = []
        
        for ind in range(len(grid[0])):
            temp = []
            for ind2 in range(len(grid)):
                temp.append(grid[ind2][ind])
                
            grid2.append(temp)
            
        for row in grid2:
            row = tuple(row)
            if row in dic:
                count += dic[row]
            
        return count
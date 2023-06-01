class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        rows = len(triangle)

        for row in range(rows-1,0,-1):
            for i in range(len(triangle[row])-1):
                    triangle[row-1][i] += min(triangle[row][i],triangle[row][i+1])
                    
        return triangle[0][0]
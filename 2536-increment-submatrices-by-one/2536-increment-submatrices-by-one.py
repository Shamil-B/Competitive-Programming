class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        mat = [[0 for i in range(n)] for j in range(n)]
        
        
        for q in queries:
            for row in range(q[0],q[2]+1):
                mat[row][q[1]] += 1
                
                if q[3]+1 < n:
                    mat[row][q[3]+1] -= 1
                    
        for row in range(n):
            for ind in range(1,n):
                mat[row][ind] += mat[row][ind-1]
                
        return mat
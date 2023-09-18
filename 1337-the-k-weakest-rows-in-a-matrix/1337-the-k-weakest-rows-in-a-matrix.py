class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        for i in range(len(mat)):
            count = 0
            for j in range(len(mat[i])):
                if mat[i][j]:
                    count += 1
                    
            mat[i] = (count,i)
            
        mat.sort()
        ans = []
        for i in range(k):
            ans.append(mat[i][1])
            
        return ans
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n = len(image)
        m = len(image[0])

        def dfs(cor,visited = None):
            nonlocal n,m,color
            if not visited:
                visited = set()

            i = cor[0]
            j = cor[1]
            curColor = image[i][j]
            image[i][j] = color
            
            visited.add((i,j))
            if i>0 and image[i-1][j]==curColor:
                if (i-1,j) not in visited:
                    dfs((i-1,j),visited)
                    
            if j>0 and image[i][j-1]==curColor:
                if (i,j-1) not in visited:
                    dfs((i,j-1),visited)
                    
            if i<n-1 and image[i+1][j]==curColor:
                if (i+1,j) not in visited:
                    dfs((i+1,j),visited)
                    
            if j<m-1 and image[i][j+1]==curColor:
                if (i,j+1) not in visited:
                    dfs((i,j+1),visited)
                    
        dfs((sr,sc))
        return image
                
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        
        elif numRows == 2:
            return [[1],[1,1]]
        
        orig = [[1],[1,1]]
        
        for i in range(numRows-2):
            temp = [1]
            
            for i in range(numRows-2):
                if i+1<len(orig[-1]):
                    temp.append(orig[-1][i] + orig[-1][i+1])
                
            temp.append(1)
            orig.append(temp)
            
        return orig
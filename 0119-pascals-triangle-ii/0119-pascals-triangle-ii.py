class Solution:
    def getRow(self, row):
        if row == 0:
            return [1]
        
        arr = self.getRow(row-1)

        newArr = [1]
        for i in range(1,row+1):
            left = arr[i-1]
            if i >= row:
                cur = 0
            else:
                cur = arr[i]
            newArr.append(left+cur)
                        
        return newArr
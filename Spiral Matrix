class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        while len(matrix)>0:
            res = self.moveRight(matrix,res)
            matrix = matrix[1:]

            res = self.moveDown(matrix,res)
            for row in range(len(matrix)):
                if len(matrix[row])>0:
                    matrix[row].pop()

            res = self.moveLeft(matrix,res)
            matrix = matrix[:-1]

            res = self.moveUp(matrix,res)
            for row in range(len(matrix)-1,-1,-1):
                matrix[row] = matrix[row][1:]

        return res

    def moveRight(self,matrix,res):
        if len(matrix)>0 and len(matrix[0])>0:
            for i in range(len(matrix[0])):
                res.append(matrix[0][i])

        return res

    def moveDown(self,matrix,res):
        if len(matrix)>0 and len(matrix[0])>0:
            for i in range(len(matrix)):
                res.append(matrix[i][-1])

        return res

    def moveLeft(self,matrix,res):
        if len(matrix)>0 and len(matrix[-1])>0:
            for i in range(len(matrix[-1])-1,-1,-1):
                res.append(matrix[-1][i])

        return res

    def moveUp(self,matrix,res):
        if len(matrix)>0 and len(matrix[0])>0:
            for i in range(len(matrix)-1,-1,-1):
                res.append(matrix[i][0])

        return res

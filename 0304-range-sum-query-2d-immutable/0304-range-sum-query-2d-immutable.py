class NumMatrix:

    def __init__(self, matrix):
        self.matrix = matrix
        pfs1 =pfs2 = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        pfs1[0] = matrix[0]
        for i in range(len(matrix[0])):
            for j in range(1,len(matrix)):
                pfs1[j][i] = matrix[j][i]+pfs1[j-1][i]

        for i in range(len(matrix)):
            pfs2[i][0] = pfs1[i][0]
       
        for i in range(len(matrix)):
            for j in range(1,len(matrix[0])):
                pfs2[i][j] = pfs1[i][j]+pfs2[i][j-1]

        self.pfs1 = pfs1
        self.pfs2 = pfs2



    def sumRegion(self, row1, col1, row2, col2):
        if col1-1<0:
            p1 = 0
        else:
            p1 = self.pfs2[row2][col1-1]
        if row1-1<0:
            p2 = 0

        else:
            p2 = self.pfs2[row1-1][col2]

        if row1-1<0 or col1-1<0:
            p3 = 0

        else:
            p3 = self.pfs2[row1-1][col1-1]

        p0 = self.pfs2[row2][col2]

        return p0 - p1- p2 + p3
        
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][j] = 1.5
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1.5:
                    matrix[i][j] = 0
                    for k in range(len(matrix)):
                        if matrix[k][j]!=1.5:
                            matrix[k][j] = 0
                    for l in range(len(matrix[0])):
                        if matrix[i][l]!=1.5:
                            matrix[i][l] = 0
                
        
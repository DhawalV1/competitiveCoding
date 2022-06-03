class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
       
        m = len(matrix)
        n = len(matrix[0])
        i = 0
        while i < n:
            if matrix[0][i] == 0:
                count = 5
                break
            else:
                count = 4
            i = i + 1

        j = 0
        while j < m:
            if matrix[j][0] == 0:
                count1 = 6
                break
            else:
                count1 = 3
            j = j+1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                        matrix[0][j] = matrix[i][0] = 0


        for j in range(1,n):
            if matrix[0][j] == 0:
                for i in range(1,m):
                    matrix[i][j] = 0

        for i in range(1,m):
            if matrix[i][0] == 0:
                for j in range(1,n):
                        matrix[i][j] = 0


        if count==5:
            for i in range(n):
                matrix[0][i] = 0

        if count1 == 6:
            for i in range(m):
                matrix[i][0] = 0
                    
        
        
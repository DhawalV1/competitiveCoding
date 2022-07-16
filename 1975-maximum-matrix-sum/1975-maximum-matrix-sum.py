class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        count = 0
        sum = 0
        n = False
        mini = float('inf')
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i][j] == 0:
                    n = True
                
                if matrix[i][j] < 0:
                    count += 1
                    mini = min(abs(matrix[i][j]),mini)
                    sum -= matrix[i][j]
                else:
                    sum += matrix[i][j]
                    mini = min(abs(matrix[i][j]),mini)
        if n == True:
            return sum
        else:
            
            if count % 2 == 1:
                return sum - 2*mini
            else:
                return sum

class Solution:
    def numSpecial(self, A: List[List[int]]) -> int:
        
        M = len(A)
        N = len(A[0])
        row = [0] * M
        col = [0] * N
        for i in range(M):
            for j in range(N):
                if A[i][j]:
                    row[i] += 1
                    col[j] += 1
                    
        cnt = 0
        for i in range(M):
            for j in range(N):
                if A[i][j] and row[i] == 1 and col[j] == 1:
                    cnt += 1
        return cnt
                    
        
class Solution:
    def checkIfPrerequisite(self, n: int, p: List[List[int]], queries: List[List[int]]) -> List[bool]:
        con = [[False]*n for _ in range(n)]
        
        for i,j in p:
            con[i][j] = True
            
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    con[i][j] = con[i][j] or (con[i][k] and con[k][j])
                    
        return [con[i][j] for i,j in queries]
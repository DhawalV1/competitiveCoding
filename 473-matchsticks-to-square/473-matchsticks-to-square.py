class Solution:
    def makesquare(self,x: List[int]) -> bool:
        if sum(x)%4!=0:
            return False
        if len(x)<4:
            return False
        
        sides = sum(x)//4
        n = len(x)
        squareside = [0,0,0,0]
        x.sort(reverse=True)
        
        def dfs(i):
            if i == n:
                a = squareside[0]
                b = squareside[1]
                c = squareside[2]
                d = squareside[3]
                return sides == a == b == c == d
            for si in range(4):
                if squareside[si] + x[i] > sides:
                    continue
                squareside[si] += x[i]
            
                if dfs(i+1):
                    return True
            
                squareside[si] -= x[i]
            
            return False
    
        return dfs(0)
        
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        p = []
        if n%2==0:
            for i in range(1,n//2+1):
                if n%i==0:
                    p.append(i)
            p.append(n)
        else:
            for i in range(1,2*n//3):
                if n%i==0:
                    p.append(i)
            p.append(n)
        
        if len(p)>=k:
            return p[k-1]
        else:
            return -1
                
            
        
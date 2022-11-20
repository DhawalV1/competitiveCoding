class Solution:
    def checkRecord(self, n: int) -> int:
        m = 1000000007
        if n == 1:
            return 3
        if n == 2:
            return 8
        p = [0]*n
        l = [0]*n 
        a = [0]*n
        
        p[0] = 1
        l[0] = 1
        a[0] = 1
        l[1] = 3
        a[1] = 2
        a[2] = 4
        
        for i in range(1,n):
            p[i] = (p[i-1]%m + a[i-1]%m + l[i-1]%m)%m
            if i>1: l[i] = (p[i-1]%m + p[i-2] + a[i-1]%m + a[i-2]%m)%m
            if i>2: a[i] = (a[i-1]%m + a[i-2]%m + a[i-3]%m)%m
            
        return (p[-1]+a[-1]+l[-1])%m
            
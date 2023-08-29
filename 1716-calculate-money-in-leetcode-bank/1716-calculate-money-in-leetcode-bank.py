class Solution:
    def totalMoney(self, n: int) -> int:
        
        m = n//7
        
        if n<8:
            return n*(n+1)//2
        
        l = 28*m+7*(m*(m-1)//2)
        i = 7*m
        while i<n:
            l += m+1
            m += 1
            i += 1
            
        return int(l)
        
        
        
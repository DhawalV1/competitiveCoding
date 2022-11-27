class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n == 0:return 0
        m = 0
        while n>0:
            n //= 5
            m += n
        return m
        '''
        if n == 0: return 0
        m1 = n//5
        m2 = n//25
        m3 = (n//125)
        m4 = (n//625)
        m5 = n//3125
        
        
        return m1 + m2 + m3 + m4 + m5
        
        '''
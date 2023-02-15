class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        mod = 1000000007
        gcd = math.gcd(a,b)
        l = 2
        r = 10**14
        lcm = a*b//gcd
        
        while l<r:
            
            m = (l+r)//2
            
            if m//a + m//b - m//lcm < n:
                
                l = m + 1
                
            else:
                
                r = m
                
        return l%mod
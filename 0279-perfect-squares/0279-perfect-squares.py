class Solution:
    def numSquares(self, n: int) -> int:
        
        if self.squ(n): return 1
        
        while(n&3==0):
            n = n>>2
        if (n&7==7):
            return 4
        sqrt = int(n**0.5)
        j = 1
        while(j<=sqrt):
            if self.squ(n-j*j): return 2
            j += 1
        return 3
        
    def squ(self,p):
        return int(math.sqrt(p))*int(math.sqrt(p)) == p
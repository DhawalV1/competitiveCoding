class Solution:
    def countDigitOne(self, n: int) -> int:
        
        
        if(n<1): return 0
        if(n>=1 and n<10): return 1
        
        y=1
        x=n
        while x>=10:
            x//=10
            y*=10
        
        if(x==1):
            return n-y+1+self.countDigitOne(y-1)+self.countDigitOne(n%y)
        else:
            return y+self.countDigitOne(y-1)*x+self.countDigitOne(n%y)
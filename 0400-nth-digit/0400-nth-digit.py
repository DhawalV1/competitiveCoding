class Solution:
    def findNthDigit(self, n: int) -> int:
        
        start, digits = 1, 1
        while n > 9 * start * digits:
            n -= 9 * start * digits
            start = 10 ** digits
            digits += 1
            
        return int(str(start + (n-1)//digits)[(n-1) % digits])
        
    def findNth(self,n):
        
        if n<10:return n
        return (n - 10**int(math.log(n,10)) + 1)*(int(math.log(n,10))+1) + self.findNth(10**int(math.log(n,10)) - 1)
        
        
class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'
        d = '0123456789abcdef'
        
        p = ''
        i = 0
        while i<8:
            rem = num%16
            p = d[rem] + p
        
            num >>= 4
            i += 1
            
        return p.lstrip('0')
                
        
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        '''
        q,r = divmod(abs(n),abs(d))
        sign = '-' if n*d<0 else ''
        ans = sign + str(q)
        dec = ''
        if r == 0: return ans
        rs = {}
        i = 0
        while r>0 and r not in rs:
            rs[r] = i
            q,r = divmod(r*10,d)
            dec += str(q)
            i += 1
            
        if r in rs:
            i = rs[r]
            return ans + '.' + dec[:i] + '(' + dec[i:] + ')'
        
        else:
            return ans + '.' + dec[:]
        '''
        n, remainder = divmod(abs(numerator), abs(denominator))
        sign = '-' if numerator * denominator < 0 else ''
        integer = sign + str(n)
        if remainder == 0: return integer
        
        rs = {}       
        decimal = ''
        i = 0
        while remainder > 0 and remainder not in rs:
            rs[remainder] = i
            n, remainder = divmod(remainder*10, abs(denominator))
            decimal += str(n)
            i +=  1
        
        if remainder in rs:
            i = rs[remainder]
            return integer + '.' + decimal[:i] + '(' + decimal[i:] + ')'
        else:
            return integer + '.' + decimal[:]
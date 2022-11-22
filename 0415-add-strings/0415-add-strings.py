class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        if len(num1)<len(num2):
            return self.addStrings(num2,num1)
        
        m = len(num1)
        n = len(num2)
        num2 = (m-n)*'0' + num2
        p = ''
        i = m-1
        j = n-1
        print(num2)
        carry = 0
        
        while (i>=0):
            t = int(num1[i])+int(num2[i]) + carry
            rem = t%10
            p = str(rem) + p
            if t>9:
                carry = 1
            else:
                carry = 0
            i -= 1
            
        if carry == 1:
            return str(1) + p
        return p
            
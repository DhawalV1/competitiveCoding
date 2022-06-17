class Solution:
    def intToRoman(self, num: int) -> str:
        m = num//1000
        num %= 1000
        c = num//100
        num %= 100
        x = num//10
        num %= 10
        i = num
        
        roman = ''
        
        if i<4:
            roman = 'I'*i + roman
        elif i==4:
            roman = 'IV' + roman
        elif i<9:
            roman = 'V'+'I'*(i%5) + roman
        else:
            roman = 'IX' + roman
            
        if x<4:
            roman = 'X'*x + roman
        elif x==4:
            roman = 'XL' + roman
        elif x<9:
            roman = 'L'+'X'*(x%5) + roman
        else:
            roman = 'XC' + roman
            
        if c<4:
            roman = 'C'*c + roman
        elif c==4:
            roman = 'CD' + roman
        elif c<9:
            roman = 'D'+'C'*(c%5) + roman
        else:
            roman = 'CM' + roman
            
        roman = 'M'*m + roman
        
        # print(roman, i, x, c, m)
        return roman
        
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0: return '0'
        p = ''
        if num>0:
            while (num!=0):
                p = '{}'.format(num%7) + p
                num //= 7

            return p
        else:
            num *= -1
            while (num!=0):
                p = '{}'.format(num%7) + p
                num //= 7
            p = '-' + p
            return p
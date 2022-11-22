class Solution:
    def addDigits(self, num: int) -> int:
        sumi = num
        while(sumi//10!=0):
            temp = sumi
            sumi = 0
            while(temp!=0):
                sumi += temp%10
                temp //= 10
                
                
        return sumi
        
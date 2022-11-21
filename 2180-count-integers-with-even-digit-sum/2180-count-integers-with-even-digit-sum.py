class Solution:
    def countEven(self, num: int) -> int:
        sumi = 0
        tmp = num
        while(num):
            sumi += num%10
            num //= 10
            
        return int((tmp - sumi%2)/2)
            
            
        
        
        
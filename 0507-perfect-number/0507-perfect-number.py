class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        
       
        sumi = 1
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                sumi += i + num//i if i<<num//i else 0
        sumi += num**0.5 if int(num**0.5) == num**0.5 else 0
                
                
        
        return sumi == num
                
            
class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        
        ans = 0
        
        while bin(num1).count('1') > ans:
            
            ans += 1
            num1 -= num2
            
            if num1<ans:
                return -1
            
        return ans
class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        
        ans = ''
        while a+b>0:
            if ans[-2:] == 'aa':
                b -= 1
                ans += 'b'
            elif ans[-2:] == 'bb':
                a -= 1
                ans += 'a'
            elif a>=b:
                a -= 1
                ans += 'a'
            else:
                b -= 1
                ans += 'b'
                
        return ans
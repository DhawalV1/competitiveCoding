class Solution:
    def reverse(self, x: int) -> int:
        if x>=0:
            
            if int(str(x)[::-1]) > 2147483647:
            
                return 0
            else:
                return int(str(x)[::-1])
        else:
            if int(str(-x)[::-1]) > 2147483648:
            
                return 0
            else:
                return -int(str(-x)[::-1])
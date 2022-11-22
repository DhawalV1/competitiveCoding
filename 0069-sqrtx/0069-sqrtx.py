class Solution:
    def mySqrt(self, x: int) -> int:
        
        for i in range(0,46342):
            if i*i<x:
                continue
            else:
                if i*i==x:
                    return i
                else:
                    return i-1
        
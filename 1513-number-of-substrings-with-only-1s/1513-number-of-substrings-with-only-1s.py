class Solution:
    def numSub(self, s: str) -> int:
        
        mod = 1000000007
        count = 0
        i = 0
        for dig in s:
            if dig == '0':
                
                i = 0
                
            else:
                
                i = (i + 1)
                count = (count + i)%mod
                
        return count%mod
        
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        res = 0
        count = 0
        i = 0
        while i<len(s):
            
            if s[i] == 'L':
                count += 1
            if s[i] == 'R':
                count -= 1
                
            if count == 0:
                res += 1
            i += 1 
        return res
class Solution:
    def countSegments(self, s: str) -> int:
        s += ' '
        count = 0
        if s == '':return 0
        for i in range(len(s)):
            
            if s[i] != ' ' and s[i+1]==' ':
                count += 1
             
        return count 
        
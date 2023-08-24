class Solution:
    def makeFancyString(self, s: str) -> str:
        
        if len(s)<3:
            return s
        
        i = 0
        j = 1
        k = 2
        
        p = s[0:2]
        
        while k<len(s):
            
            if not s[i]==s[j] or not s[j]==s[k]:
                
                p += s[k]
                
            i += 1
            j += 1
            k += 1
            
        return p
                
                
        
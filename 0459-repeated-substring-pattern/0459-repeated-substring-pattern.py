class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        p = len(s)
        factor = []
        for i in range(1,p//2+1):
            if p%i==0:
                factor.append(i)
        count = 0        
        for k in factor:
            i = 0
            while(i<len(s) and i+k<=len(s) and i+2*k<=len(s)):
                if s[i:i+k]==s[i+k:i+2*k]:
                    count = 1
                    
                else:
                    
                    count = 0
                    break
                i += k
            if count==1: return True
        
        return False
                    
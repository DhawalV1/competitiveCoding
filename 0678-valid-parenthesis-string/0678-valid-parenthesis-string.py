class Solution:
    def checkValidString(self, s: str) -> bool:
        cmax = 0
        cmin = 0
        
        for i in s:
            
            if i == '(':
                l = 1
                cmax += 1
                cmin += 1
                
            elif i == ')':
                cmax -= 1
                cmin -= 1
            else:
                cmax += 1
                cmin -= 1
                
            if cmax<0: return False
            
            cmin = max(0,cmin)
        
                
                
    
        
        
        return cmin==0
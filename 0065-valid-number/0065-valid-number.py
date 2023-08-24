class Solution:
    def isNumber(self, s: str) -> bool:
        
        s = s.strip()
        dot = exp = dig = False
        for i,c in enumerate(s):
            
            if c in ['+','-']:
                if i>0:
                    if s[i-1] not in 'eE': 
                        return False
            
            elif c=='.':
                if dot == True:
                    return False
                
                dot = True
                if exp == True:
                    return False
                
            elif c in 'eE':
                if exp or not dig:
                    return False
                
                exp = True
                dig = False
            elif c.isdigit():
                dig = True
            else:
                return False
                
        return dig
            
            
                
        
        
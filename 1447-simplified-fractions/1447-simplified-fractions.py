class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        
        if n == 1:return []
        a = []
        for l in range(2,n+1):
            
            for m in range(1,n):
                
                if math.gcd(m,l)==1 and m!=1 and l>m:
                    
                    a.append('{}/{}'.format(m,l))
                    
                elif m == 1:
                    
                    a.append('{}/{}'.format(m,l))
                    
                    
                    
        return a
            
            
        
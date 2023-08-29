class Solution:
    def bestClosingTime(self, customers: str) -> int:
        sumi = 0
        for i in customers:
            if i == 'N':
                
                sumi += 1
                
                
        p = [sumi]
        
        for i in customers[::-1]:
            
            if i == 'Y':
                sumi += 1
                p.append(sumi)
                
            else:
                
                sumi -= 1
                
                p.append(sumi)
        minv = min(p)
        return p[::-1].index(minv)
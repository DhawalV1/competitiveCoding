class Solution:
    def calPoints(self, op: List[str]) -> int:
        rec = []
        sumi = 0
        for i in op:
            
            if i=='C':
                sumi -= int(rec[-1])
                rec.pop()
                
                
            elif i=='D':
                
                rec.append(2*int(rec[-1]))
                
                sumi += rec[-1]
                
            elif i=='+':
                
                rec.append(int(rec[-1])+int(rec[-2]))
                sumi += rec[-1]
                
            else:
                
                rec.append(i)
                sumi += int(i)
                
                
        return sumi
                
                
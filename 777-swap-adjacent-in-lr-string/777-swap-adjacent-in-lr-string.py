class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        
        if len(start)!=len(end):
            return False
        if len(start)==1 and start!=end:
                return False
        s = [i for i in start if i!='X']
        e = [i for i in end if i!='X']
        if s!=e:
            return False
        d = {}
        d1 = {}
        '''
        for i in start:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
                
        for i in end:
            if i in d1:
                d1[i] += 1
            else:
                d1[i] = 1
        if d.get('L')!=d1.get('L') or d.get('R')!=d1.get('R') or d.get('X')==None:
            return  False
        '''
        n = len(start)
        
        Lstart = [i for i in range(n) if start[i] == 'L']
        Lend = [i for i in range(n) if end[i] == 'L']
        
        Rstart = [i for i in range(n) if start[i] == 'R']
        Rend = [i for i in range(n) if end[i] == 'R']
        
        for i, j in zip(Lstart, Lend):
            if i < j:
                return False
            
        for i, j in zip(Rstart, Rend):
            if i > j:
                return False
            
        return True
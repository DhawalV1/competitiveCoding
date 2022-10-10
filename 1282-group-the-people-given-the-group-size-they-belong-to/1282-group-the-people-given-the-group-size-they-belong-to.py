class Solution:
    def groupThePeople(self, g: List[int]) -> List[List[int]]:
        p = []
        for i,y in enumerate(g):
            p.append([y,i])
            
        p.sort()
        l = []
        m = 0
        while m < len(p):
            q = []
            j = p[m][0]
            while j>0:
                q.append(p[m][1])
                j -= 1
                m += 1
                
            l.append(q)
            
            
            
        return l
        
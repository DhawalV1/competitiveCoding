class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0],-x[1]))
        searchi = []
        for i in range(len(envelopes)):
            searchi.append(envelopes[i][1])
        sub = []
        for x in searchi:
            if len(sub)==0 or sub[-1]<x:
                sub.append(x)
            else:
                idx = bisect_left(sub,x)
                sub[idx] = x
        return len(sub)
            
            
            
            
            
   
            
            
        
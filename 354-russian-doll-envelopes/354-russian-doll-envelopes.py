class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0],-x[1]))
        
        
        sub = []
        sub.append(envelopes[0][1])
        for i in range(1,len(envelopes)):
            
            if sub[-1]<envelopes[i][1]:
                sub.append(envelopes[i][1])
            else:
                idx = bisect_left(sub,envelopes[i][1])
                sub[idx] = envelopes[i][1]
        return len(sub)
            
            
            
            
            
   
            
            
        
class Solution:
    def maxLength(self,A: List[str]) -> int:
        dp = [set()]
        for a in A:
            if len(set(a)) < len(a): continue
            a = set(a)
            for c in dp:
                if a & c: continue
                dp.append(a | c)
        return max(len(a) for a in dp)
    
    
    
    
    '''
    maxlen = 0
        unique = ['']
        
        def isvalid(s):
            return len(s) == len(set(s))
        
        for word in arr:
            for j in unique:
                tmp = word + j
                if isvalid(tmp):
                    unique.append(tmp)
                    maxlen = max(maxlen, len(tmp))
                    
        return maxlen
        
        
    '''
        
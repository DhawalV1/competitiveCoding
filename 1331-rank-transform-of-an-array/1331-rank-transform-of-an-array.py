class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        d = {}
        num = arr.copy()
        
        num.sort()
        
        a = []
        
        rank = 1
        
        for i in num:
            
            if i not in d:
                
                d[i] = rank
                
                rank += 1
                
        for i in arr:
            
            a.append(d[i])
            
            
        return a
                
                
                
            
            
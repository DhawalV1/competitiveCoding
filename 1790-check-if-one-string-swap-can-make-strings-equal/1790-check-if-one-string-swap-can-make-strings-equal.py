class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        
        seen = []
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                seen.append([s1[i],s2[i]])
                
                
                
        
        return len(seen)==0 or len(seen)==2 and seen[0]==seen[1][::-1]
            
class Solution:
    def minOperations(self, s: str) -> int:
        
        dp1 = [str(i&1) for i in range(len(s))]
        dp2 = [str((i+1)&1) for i in range(len(s))]
        count1 = 0
        count2 = 0
        
        for i in range(len(s)):
            
            if s[i]!=dp1[i]:
                
                count1 += 1
                
            if s[i]!=dp2[i]:
                
                count2 += 1
                
        return min(count1,count2)
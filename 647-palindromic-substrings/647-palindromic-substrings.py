class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        n = len(s)
        def palini(i,j):
            res = 0
            while i>=0 and j<n:
                if s[i]!=s[j]:
                    return res
                i -= 1
                j +=1
                res += 1
            
            return res
        
        for i in range(n):
            res += palini(i,i) + palini(i-1,i)
            
        return res
            
        
        
        
        
        
        
        
        
        
        count = 0
        for i in range(len(s)):
            for j in range(i,len(s)):
                if self.ispal(s[i:j+1]):
                    count = count+1
        return count
    def ispal(self,s):
        return s == s[::-1]
            
        
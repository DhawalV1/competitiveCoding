class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        r, c, l= len(s1), len(s2), len(s3)
        if r+c != l:
            return False
        dp = [True for _ in range(c+1)] 
        for j in range(1, c+1):
            dp[j] = dp[j-1] and s2[j-1] == s3[j-1]
        for i in range(1, r+1):
            dp[0] = (dp[0] and s1[i-1] == s3[i-1])
            for j in range(1, c+1):
                dp[j] = (dp[j] and s1[i-1] == s3[i-1+j]) or (dp[j-1] and s2[j-1] == s3[i-1+j])
        return dp[-1]
            
        
        
    """
        return self.helper(s1,s2,s3) or self.helper(s2,s1,s3)
    def helper(self,s1,s2,s3):
        m = len(s1)
        n = len(s2)
        p = len(s3)
        
        if m==0 or n==0:
            return s1==s3 or s2==s3
        
        i = 0
        j = 0
        k = 0
        
        if m + n != p:
            return False
        
        while i<m and j<n:
            
            
            if s1[i] == s3[k]:
                i += 1
                k += 1
            elif s2[j] == s3[k]:
                j += 1
                k += 1
            else:
                return False
                    
        return True 
        
        r, c, l= len(s1), len(s2), len(s3)
        if r+c != l:
            return False
        dp = [[True for _ in range(c+1)] for _ in range(r+1)]
        for i in range(1, r+1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
        for j in range(1, c+1):
            dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]
        for i in range(1, r+1):
            for j in range(1, c+1):
                dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i-1+j]) or \
                   (dp[i][j-1] and s2[j-1] == s3[i-1+j])
        return dp[-1][-1]
        """
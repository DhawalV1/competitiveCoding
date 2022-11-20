class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        def solve(s1,s2,i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            if i == len(s1) and j == len(s2):
                return 0
            if i == len(s1):
                return len(s2)-j
            if j == len(s2):
                return len(s1)-i
            if (i,j) not in memo:
                if s1[i] == s2[j]:
                    ans = solve(s1,s2,i+1,j+1)
                    
                else:
                    ins = 1 + solve(s1,s2,i+1,j)
                    dele = 1 + solve(s1,s2,i,j+1)
                    rep = 1 + solve(s1,s2,i+1,j+1)
                    ans = min(ins,dele,rep)
                    
                memo[(i,j)] = ans
                
            return ans
        
        return solve(word1,word2,0,0)
            
        
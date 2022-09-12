class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        result = 1
        dp = {}
        for word in words:
            dp[word] = 1
            
            for i in range(len(word)):
                prev = word[:i] + word[i+1:]
                
                if prev in dp:
                    dp[word] = max(dp[prev]+1,dp[word])
                    
                    result = max(result,dp[word])
                    
                    
        return result
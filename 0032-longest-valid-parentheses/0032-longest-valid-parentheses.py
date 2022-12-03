class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        left = 0
        right = 0
        maxi = 0
        for i in s:
            if i == '(':
                left += 1
            else:
                right += 1
            if left == right: maxi = max(maxi,2*right)
            elif right>=left: 
                left = 0
                right = 0
                
                
        left = 0
        right = 0
        
        for i in range(len(s)-1,-1,-1):
            if s[i] == '(':
                left += 1
            else:
                right += 1
            if left == right: maxi = max(maxi,2*left)
            elif right<=left: 
                left = 0
                right = 0
                
        return maxi
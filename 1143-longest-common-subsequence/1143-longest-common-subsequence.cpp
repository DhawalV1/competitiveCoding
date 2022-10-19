class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        int m = text1.length();
        int n = text2.length();
        
        short dp[2][1000] = {};
        for(int i=0;i<m;i++) {
            for(int j=0;j<n;j++) {
                dp[!(i%2)][j+1] = text1[i]==text2[j]?dp[i%2][j]+1:max(dp[i%2][j+1],dp[!(i%2)][j]);
                
            }
            
        
        }
        return dp[m%2][n];        
    }
};
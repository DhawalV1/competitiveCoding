class Solution {
public:
    int maxUncrossedLines(vector<int>& nums1, vector<int>& nums2) {
        int dp[2][500];
        int m = nums1.size(), n = nums2.size();
        memset(dp,0,sizeof dp);
        
        for(int i=0;i<m;i++) {
            for(int j=0;j<n;j++) {
                dp[!(i%2)][j+1] = nums1[i]==nums2[j]?dp[i%2][j]+1:max(dp[i%2][j+1],dp[!(i%2)][j]);
                
            }
            
        
        }
        return dp[m%2][n];  
        
    }
};
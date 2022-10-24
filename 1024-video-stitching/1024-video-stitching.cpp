class Solution {
public:
    int videoStitching(vector<vector<int>>& clips, int T) {
        int n = clips.size();
        int i, j;
        
        vector<int> dp = vector<int>(n + 1, -1);
        dp[0] = 0;
        for (i = 1; i <= n; i++) {
            dp[i] = dp[i-1];
            for (j = 0; j < n; j++) {
                if (clips[j][0] <= dp[i-1]) {
                    dp[i] = max(dp[i], clips[j][1]);
                }
            }
        }
        
        for (i = 1; i <= n; i++) {
            if (dp[i] >= T) {
                return i;
            }
        }
        return -1;
    }
};
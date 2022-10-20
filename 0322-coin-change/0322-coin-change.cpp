class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        vector<int> dp(amount+1,INT_MAX);
        dp[0] = 0;
        for(int i = 0;i<dp.size();i++)
            for(auto& c:coins)
                if(c<=i)
                    if(dp[i-c]!=INT_MAX)
                        dp[i] = min(dp[i-c]+1,dp[i]);
        
        return dp[dp.size()-1]==INT_MAX?-1: dp[dp.size()-1];
    }
};
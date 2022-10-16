class Solution {
public:
    int minDifficulty(vector<int>& j, int days) {
        
        int n = j.size();
        if (n<days) return -1;
        vector<int> dp(n),old(n);
        
        dp[0] = j[0];
        for(int i = 1;i<n;i++)
            dp[i] = max(dp[i-1],j[i]);
        
        for(int d = 1;d<days;d++) {
            swap(dp,old);
            
            vector<array<int,3>> stk = {{1<<30,1<<30,1<<30}};
            for(int i = d;i<n;i++) {
                int oldbest = old[i-1];
                while(stk.back()[1] <= j[i]) {
                    oldbest = min(oldbest,stk.back()[0]);
                    stk.pop_back();
                }
                stk.push_back({oldbest,j[i],min(oldbest+j[i],stk.back()[2])});
                dp[i] = stk.back()[2];
                
                
            }
        }
        return dp[n-1];
        
        
    }
};
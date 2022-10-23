class Solution {
public:
    bool PredictTheWinner(vector<int>& nums) {
        int n = nums.size();
        vector<vector<int>>dp(n+1,vector<int>(n+1,-1));
        int score = solve(nums,0,n-1,dp);
        int sum = accumulate(begin(nums),end(nums),0);
        return score>=sum-score;
    
        
    }
private:
    int solve(vector<int>& nums,int i,int j,vector<vector<int>>& dp) {
        if(i>j) return 0;
        if (i==j) return nums[i];
        if (dp[i][j]!=-1) return dp[i][j];
        int cur = max(nums[i] + min(solve(nums,i+2,j,dp),solve(nums,i+1,j-1,dp)),nums[j] + min(solve(nums,i+1,j-1,dp),solve(nums,i,j-2,dp)));
        dp[i][j] = cur;
        return cur;
        
    }
};
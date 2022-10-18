class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int ts = accumulate(begin(nums),end(nums),0);
        if(ts%2==1) return false;
        int hs = ts/2;
        bool dp[hs+1]; memset(dp,false,sizeof dp);
        dp[0] = true;
        for(int num : nums)
            for(int j = hs;j>= num;j--)
                if(dp[j-num])
                    dp[j] = true;
        
        return dp[hs];
    }
};
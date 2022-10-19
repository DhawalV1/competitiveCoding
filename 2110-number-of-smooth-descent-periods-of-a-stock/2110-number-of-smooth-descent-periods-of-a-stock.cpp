class Solution {
public:
    long long getDescentPeriods(vector<int>& prices) {
        long long count = 1,dp = 1;
        for(int i = 0;i<prices.size()-1;i++) {
            if(prices[i]-1==prices[i+1]) dp++;
            else dp = 1;
            
            count += dp;
        }
        
        return count;
        
        
        
    }
};
class Solution {
public:
    string minWindow(string s, string t) {
            int i = 0, j = 0, n = s.size(), si = -1, ei = -1;
    
    vector<int> dp(127, 0);
    for(auto &i : t)
        dp[i]--;
    
    while(j < n)
    {
        dp[s[j++]]++;
        while(i < j && dp[s[i]] > 0)
            dp[s[i++]]--;
        
        if((si == -1 || j - i < ei - si) && check(dp))
            si = i, ei = j;
    }
    
    string ans;
    while(si < ei)
        ans += s[si++];
    
    return ans;
}

bool check(vector<int> &dp)
{        
    for(int i = 0; i < 127; i++)
        if(dp[i] < 0)
            return false;
    
    return true;
}
    
};
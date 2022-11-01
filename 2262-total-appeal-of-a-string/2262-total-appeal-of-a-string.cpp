class Solution {
public:
    long long appealSum(string s) {
        long long res = 0,cur = 0;
        vector<int> seen(26);
        for(int i = 0;i<s.length();i++) {
            cur += i + 1- seen[s[i]-'a'];

            seen[s[i]-'a'] = i+1;
            
            res += cur;
            
        }
        return res;
    }
};
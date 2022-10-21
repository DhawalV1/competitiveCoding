class Solution {
public:
    int findLongestChain(vector<vector<int>>& pairs) {
        sort(pairs.begin(), pairs.end(), cmp);
        int res = 0,cur = -1001;
        for(auto &p:pairs) {
            if (p[0]>cur) {
                cur = p[1];
                res++;
            }
        }
        return res;
    }
private:
    static bool cmp(vector<int>& a, vector<int>&b) {
        return a[1] < b[1] || a[1] == b[1] && a[0] < b[0];
    }
};
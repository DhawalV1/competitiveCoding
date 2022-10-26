class Solution {
public:
    int maxTurbulenceSize(vector<int>& A) {
        if (A.size() == 0) return 0;
        
        int n = A.size(), maxLen = 0;
        vector<vector<int>> state(n,vector<int>(2,0));
        
        for (int i = 1; i < n; i++) {
            if (A[i - 1] < A[i]) {
                state[i][0] = state[i - 1][1] + 1;
                maxLen = max(maxLen, state[i][0]);
            } else if (A[i - 1] > A[i]) {
                state[i][1] = state[i - 1][0] + 1;  
                maxLen = max(maxLen, state[i][1]);
            }
        }
        
        return maxLen + 1;
    }
};
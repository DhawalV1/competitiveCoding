class Solution {
public:
    int maxRotateFunction(vector<int>& A) {
        
        
        int sum = 0, F0 = 0, maxi = INT_MIN;
        for (int i = 0; i < A.size(); i++) {
            sum += A [i];
            F0 += i * A [i];
        }
        vector<int> dp(A.size(),0);
        dp [0] = F0;
        maxi = dp [0];
        for (int i = 1; i < A.size(); i++) {
            dp [i] = dp [i-1] + sum - A.size()* A [A.size()- i];
            maxi = max(maxi, dp [i]);
        }
        return maxi;
    }
};
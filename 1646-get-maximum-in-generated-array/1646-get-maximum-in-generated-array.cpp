class Solution {
public:
    int getMaximumGenerated(int n) {
        if(n<2) return n;
        vector<int> nums(n+2,0);
        nums[1]=1;
        int j = 1;
        int maxi = 0;
        while (2*j<=n) {
            nums[2*j] = nums[j];
            nums[2*j+1] = nums[j]+nums[j+1];
            j++;
            
        }
        for (int k=0;k<=n;k++)
            maxi = max(nums[k],maxi);
        return maxi;
        
    }
};
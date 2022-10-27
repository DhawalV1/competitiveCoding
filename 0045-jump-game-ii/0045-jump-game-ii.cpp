class Solution {
public:
    int jump(vector<int>& nums) {
        int i = 0;
        int n = nums.size(),maxr = 0,lastpos = 0;
        int jumps = 0;
        while(lastpos < n-1) {
            
            maxr = max(maxr,nums[i]+i);
            
            if (lastpos == i) {
                lastpos = maxr;
                jumps++;
            }
            
            i++;
        }
        
        return jumps;
    }
};
class Solution {
public:
    int res=0;
    void backtrack(vector<int> &nums,int idx,int target,int sum)
    {
        if(idx>=nums.size())
        {
            if(sum==target)
                res++;
            return ;
        }
        backtrack(nums,idx+1,target,sum+nums[idx]);
        backtrack(nums,idx+1,target,sum-nums[idx]);
    }
    
    int findTargetSumWays(vector<int>& nums, int target) {
        backtrack(nums,0,target,0);
        return res;
    }
   
    
};
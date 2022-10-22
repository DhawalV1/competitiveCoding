class Solution {
public:
    int maxSumDivThree(vector<int>& nums) {
        int rem1 = 10001;
        
        
        int rem2 = 10001;
        
       
        int sum = 0;
        
        for(int i=0;i<nums.size();i++)
        {
            
            sum+=nums[i];
            
            
            if(nums[i]%3==1)rem2 = min(rem1+nums[i],rem2),rem1= min(rem1,nums[i]);
            
            
            if(nums[i]%3==2)rem1 = min(rem2+nums[i],rem1),rem2= min(rem2,nums[i]);
        }
        
        
        
        return (sum%3==0)?sum:((sum%3==1)?(sum-rem1):(sum-rem2));
    }
};
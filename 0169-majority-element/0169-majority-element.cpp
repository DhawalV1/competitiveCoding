class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int count = 1;
        int k=nums[0];
        for(int i = 1;i<nums.size();i++) {
            if (count==0) {
                count++;
                k = nums[i];
                
            }
            else if(k==nums[i]) count++;
            else {
                count--;
            }
            
            
        }
        return k;
    }
};
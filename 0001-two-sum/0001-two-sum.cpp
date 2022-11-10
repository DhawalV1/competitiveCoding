class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> mp;
        vector<int> res;
        
        for(int i = 0;i<nums.size();i++) {
            int y = target - nums[i];
            if(mp.find(y)!=mp.end()) {
                
                res.push_back(mp[y]);
                res.push_back(i);
                return res;
                
            }
            
            mp[nums[i]] = i;
        }
            
        return res;
    }
};
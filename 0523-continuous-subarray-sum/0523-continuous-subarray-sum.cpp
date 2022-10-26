class Solution {
public:
    bool checkSubarraySum(vector<int>& nums, int k) {
        unordered_map<int,int> d;
        d[0] = -1;
        int sumi = 0;
        for(int i = 0;i<nums.size();i++) {
            sumi += nums[i];
            if(k!=0) sumi %= k;
            if (d.find(sumi)!=d.end()) {
                if(i-d[sumi]>1) return true;
                
            }
            else d[sumi]=i;
        }
        
        return false;
       

    }
};
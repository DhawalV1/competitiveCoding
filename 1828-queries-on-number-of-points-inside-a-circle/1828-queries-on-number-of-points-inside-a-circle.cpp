class Solution {
private:
    int sq(int x) {return x*x;}

public:
    vector<int> countPoints(vector<vector<int>>& points, vector<vector<int>>& queries) {
        vector<int> ans;
        
        for (vector<int>q:queries) {
            int sum = 0;
            for (vector<int>p:points) {
                
                int dsq = sq(p[0]-q[0]) + sq(p[1]-q[1]);
                if (dsq <= q[2]*q[2]) {
                    sum += 1;
                }
                
            }
            
                
            ans.push_back(sum);
        }
        
        return ans;
        
    }
};
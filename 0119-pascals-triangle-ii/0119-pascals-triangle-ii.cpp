class Solution {
public:
    vector<int> getRow(int n) {
        if(n==0) {
            return {1};
        }
        if (n==1) {
            return {1,1};
        }
        int j = 2;
        vector<int> temp(2,1);
        while(j<n+1) {
            vector<int> res(1,1);
            for (int i=0;i<j-1;i++)
                res.push_back(temp[i]+temp[i+1]);
            res.push_back(1);
            temp = res;
            j++;
        }
        
        return temp;
        
    }
        
};
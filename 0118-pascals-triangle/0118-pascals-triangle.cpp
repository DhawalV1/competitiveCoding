class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        
        if(numRows == 1)
            return {{1}};
        else if(numRows == 2)
            return {{1}, {1,1}};
        vector<vector<int>> res;
        res.push_back({1});
        res.push_back({1,1});
        
        int row = 2;
        while(row < numRows) {
            vector<int> temp;
            
            
            temp.push_back(1);
            for(int i = 0; i < row-1; i++) 
                temp.push_back(res[row-1][i] + res[row-1][i + 1]);
            temp.push_back(1);
            
            res.push_back(temp);
            row++;
        }
        
        return res;
    }
};
class Solution {
public:
    int maxIncreaseKeepingSkyline(vector<vector<int>>& grid) {
        vector<int> row;
        int n = grid.size();
        int m = grid[0].size();
        vector<int> col;
        for (int i=0;i<n;i++) {
            int maxi=0;
            for (int j=0;j<m;j++) {
                maxi = max(maxi,grid[i][j]);
                
            }
            row.push_back(maxi);
        }
        
        for (int i=0;i<m;i++) {
            int maxi=0;
            for (int j=0;j<n;j++) {
                maxi = max(maxi,grid[j][i]);
                
            }
            col.push_back(maxi);
        }
        
        int sum = 0;
        for (int i=0;i<n;i++) {
            
            for (int j=0;j<m;j++) {
                
                sum += min(row[i],col[j])-grid[i][j];
            
            }
        }
        
        return sum;
    }
};
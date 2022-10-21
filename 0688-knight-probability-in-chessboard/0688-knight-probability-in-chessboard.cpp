class Solution {
private: vector<vector<int>> dir = {{-2,-1},{-1,-2},{1,-2},{2,-1},{2,1},{1,2},{-1,2},{-2,1}};

public:
    double dp[26][26][101];
    double knightProbability(int n, int k, int row, int column) {
        return find(n,k,row,column);
        
    }
public: double find(int n,int k,int r,int c){
    if(r < 0 || r > n - 1 || c < 0 || c > n - 1) return 0;
    if(k == 0)  return 1;
    if(dp[r][c][k] != 0) return dp[r][c][k];
    double rate = 0;
    for(int i = 0;i < dir.size();i++) rate += 0.125 * find(n,k - 1,r + dir[i][0],c + dir[i][1]);
    dp[r][c][k] = rate;
    return rate;
    
    }
    
};
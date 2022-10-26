class Solution {
public:
    int target;
    int closest(int a,int b) {
        if (a==0) return b;
        if(b==0) return a;
        if(abs(target-a)==abs(target-b)) { 
            return a<b?a:b; 
        }
        return abs(target-a)<abs(target-b)? a:b;
    }
    
    int helper(vector<int>& top,int i,int sum) {
        if(i>=top.size()) return sum;
        return closest(helper(top,i+1,sum+top[i]),closest(helper(top,i+1,sum+2*top[i]),helper(top,i+1,sum)));
    }
    int closestCost(vector<int>& baseCosts, vector<int>& toppingCosts, int t) {
        int ans = 0;
        target = t;
        for (int i = 0;i<baseCosts.size();i++) {
            
            ans = closest(helper(toppingCosts,0,baseCosts[i]),ans);
            
        }
        
        return ans;
        
    }
};
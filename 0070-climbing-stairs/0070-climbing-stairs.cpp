class Solution {
public:
    int climbStairs(int n) {
        
        if (n<4) {
            return n;
        }
        int a = 2,b = 3,c,j=0;
        while(j<n-3) {
            c = a+b;
            a = b;
            b = c;
            j++;
        }
        
        return c;
        
    }
};
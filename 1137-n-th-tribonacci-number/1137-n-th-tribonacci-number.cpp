class Solution {
public:
    int tribonacci(int n) {
        
        if (n<2) return n;
        if (n == 2) return 1;
        int d;
        int a=0,b=1,c=1;
        int j = 2;
        while(j<n) {
            
            d = a+b+c;
            a = b;
            b = c;
            c = d;
            j++;
            
        }
        return d;
    }   
};
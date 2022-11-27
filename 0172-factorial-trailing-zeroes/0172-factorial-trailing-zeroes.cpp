class Solution {
public:
    int trailingZeroes(int n) {
        if (n == 0) return 0;
        int m = 0;
        while (n>0) {
            n = int(n/5);
            m += n;
        }
        return m;
    }
};
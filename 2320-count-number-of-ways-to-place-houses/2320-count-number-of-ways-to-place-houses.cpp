class Solution {
public:
    typedef long long ll;
    ll mod = 1e9+7;

    int countHousePlacements(int n) {
        ll a = 1,b = 1;
        ll t = a+b;
        
        for(int i = 2;i<=n;i++) {
            a = b;
            b = t;
            t = (a+b)%mod;
        }
        return (t*t)%mod;
        
    }
};
class Solution {
public:
    long long numberOfWays(string s) {
        long long a=0,b=0,ans=0;    
        for(int i = 0; i<s.length();i++) {
            if(s[i]=='1') a++;
        }
        
        b = s.length()-a;
        long long c=0,d=0; 
        for(int i=0;i<s.length();i++){ 
            if(s[i]=='1'){ 
                ans += (d*b);
                a--;
                c++;
            }
            else {
                ans += (a*c);
                b--;
                d++;
            }
        }
        return ans;
    }
};

class Solution {
public:
    int nthSuperUglyNumber(int n, vector<int>& primes) {
        if(n==1 ) return 1;
        
        vector<long long int> ptr(primes.size(),0);
        vector<long long int> elmt(n,0);
        elmt[0]=1;
        long long int t;        
        for(int i=1; i<n ; i++){
            long long int mini=INT_MAX;
            long long int idx=0;
            for(int j=0; j<primes.size(); j++){
                t=primes[j]*elmt[ptr[j]];
                if(t<mini){
                    mini=t;
                    idx=j;
                }
            }
            for(int j=0; j<primes.size(); j++){
                if(mini==primes[j]*elmt[ptr[j]]){
                    ptr[j]++;
                }
            }
            elmt[i]=mini;
        }
        return elmt[n-1];

        }
    };
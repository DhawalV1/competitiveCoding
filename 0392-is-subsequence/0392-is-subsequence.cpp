class Solution {
public:
    bool isSubsequence(string s, string t) {
        
        int i = 0, j = t.length();
        for (int k=0;k<j;k++)
            if(t[k]==s[i]) i++;
        return s.length()==i;
        
                
        
        
        
    }
};
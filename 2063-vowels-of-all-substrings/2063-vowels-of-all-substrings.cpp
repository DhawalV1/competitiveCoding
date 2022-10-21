class Solution {
public:
    bool v[26] = {1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0};
    long long countVowels(string word) {
        long long res = 0;
        int n = word.length();
        for(int i = 0;i<n;i++) {
            res += v[word[i] - 'a'] * long (i + 1) * (n - i);            
        }
        
        return res;
    }
};
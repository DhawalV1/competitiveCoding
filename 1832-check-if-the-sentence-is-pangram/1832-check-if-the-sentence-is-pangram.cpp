class Solution {
public:
    bool checkIfPangram(string s) {
        if (s.length()<26) return false;
        set<int> umap;
        for(int i=0;i<s.length();i++)
            umap.insert(s[i]);
        return umap.size()==26;
    }
};
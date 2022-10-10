/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
private:
    int ans;
    pair<int,int> dfs(TreeNode* cur) {
        if (cur == nullptr) return {0,0};
        pair<int,int> x = {cur->val,1};
        {
            pair<int,int> y = dfs(cur->left);
            x.first += y.first;
            x.second += y.second;
        }
        {
            pair<int,int> y = dfs(cur->right);
            x.first += y.first;
            x.second += y.second;
        }
        
        if (x.first/x.second == cur->val) ++ans;
        return x;

    }
public:
    int averageOfSubtree(TreeNode* root) {
        
        ans = 0;
        dfs(root);
        return ans;
        
    }
};
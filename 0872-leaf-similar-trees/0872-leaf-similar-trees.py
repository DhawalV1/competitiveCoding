# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        ret = []
        res = []
        self.dfs(root1,ret)
        self.dfs(root2,res)
        return ret == res
        
        
    def dfs(self,node,ret):
        
        if node is None: return
        
        if node.left is None and node.right is None:
            ret.append(node.val)
            
        self.dfs(node.left,ret)
        self.dfs(node.right,ret)
        
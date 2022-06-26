# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        self.numo = 0
        self.dfs(root,targetSum)
        return self.numo
    
    def dfs(self,node,target):
        
        if node is None:
            return None
        
        self.test(node,target)
        self.dfs(node.left,target)
        self.dfs(node.right,target)
        
    def test(self,node,target):
        if node is None:
            return None
        
        if node.val==target:
            self.numo += 1
            
        self.test(node.left,target-node.val)
        self.test(node.right,target-node.val)
        
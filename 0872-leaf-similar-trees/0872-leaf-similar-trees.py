# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.findleaf(root1) == self.findleaf(root2)
        
    def findleaf(self, root):
        if not root: return []
        if not (root.left or root.right): return [root.val]
        return self.findleaf(root.left) + self.findleaf(root.right)
    '''
        ret = []
        res = []
        self.dfs(root1,ret)
        b = ret[::-1]
        self.dfs1(root2,b)
        return len(b) == 0
        
        
    def dfs(self,node,ret):
        
        if node is None: return
        
        if node.left is None and node.right is None:
            ret.append(node.val)
            
        self.dfs(node.left,ret)
        self.dfs(node.right,ret)
        
    def dfs1(self,node,ret):
        
        if node is None: return
        
        if node.left is None and node.right is None:
            if ret[-1] != node.val:
                return False
            else:
                ret.pop()
            
        self.dfs(node.left,ret)
        self.dfs(node.right,ret)
        
        
    '''
    def dfs(self,root):
        if root is None: return 
        if not(root.left or root.right) is None:return [root.val]
        return self.dfs(root.left)+self.dfs(root.right)
        
            
        
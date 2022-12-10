# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        
        sums = []
        
        def dfs(node):
            if not node:return 0
            subtree = dfs(node.left) + dfs(node.right) + node.val
            
            sums.append(subtree)
            
            return subtree
        
        m = float('-inf')
        tot = dfs(root)
        for i in sums:
            m = max(m,(tot-i)*i)
            
        return m%1000000007
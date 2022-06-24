# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        def funi(node,lo,hi):
            if not node: return hi - lo
            left = funi(node.left,lo,node.val)
            right = funi(node.right,node.val,hi)
            return min(left,right)
        
        return funi(root,float('-inf'),float('inf'))
        
        
       
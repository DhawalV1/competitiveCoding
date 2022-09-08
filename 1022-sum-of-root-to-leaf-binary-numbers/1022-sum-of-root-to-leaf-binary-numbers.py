# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        
        
        return self.sumi(root,0)
    def sumi(self,root,count):
        if root is None:
            return 0
        count = count*2 + root.val
        if root.left == root.right: return count
        return self.sumi(root.left, count) + self.sumi(root.right, count)
        
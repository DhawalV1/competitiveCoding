# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], v: int, depth: int,side="left") -> Optional[TreeNode]:
        if depth==1:
            res = TreeNode(v)
            setattr(res,side,root)
            return res
        if root:
            root.left = self.addOneRow(root.left,v,depth-1)
            root.right = self.addOneRow(root.right,v,depth-1,'right')
            
        return root
     
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        res = []
        
        def inord(node):
            
            if not node:
                return 
            inord(node.left)
            res.append(node.val)
            inord(node.right)
            
        inord(root)
        
        tree = TreeNode(res[0])
        tmp = tree
        
        for i in res[1:]:
            
            tmp.right = TreeNode(i)
            
            tmp = tmp.right
            
        return tree
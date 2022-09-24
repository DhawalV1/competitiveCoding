# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        self.helper(root,targetSum,res,[])
        return res
    def helper(self,node,t,res,path):
        if node is None:
            return 
        if node.left is None and node.right is None and t == node.val:
            path.append(node.val)
            res.append(path)
        
    
        
        self.helper(node.left,t-node.val,res,path+[node.val])
        self.helper(node.right,t-node.val,res,path+[node.val])
        
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        res = []
        if k ==0:
            res.append(target.val)
        else:
            self.dfs(res,root,target.val,k,0)
        return res
    
    def dfs(self,res,node,target,k,depth):
        
        if node is None: return 0
        
        if depth == k:
            res.append(node.val)
            return 0
        
        if node.val == target or depth >0:
            left = self.dfs(res,node.left,target,k,depth+1)
            right = self.dfs(res,node.right,target,k,depth+1)
            
        else:
            left = self.dfs(res,node.left,target,k,depth)
            right = self.dfs(res,node.right,target,k,depth)
        if node.val == target: return 1
        
        if left == k or right == k:
            res.append(node.val)
            return 0
        
        if left > 0:
            self.dfs(res,node.right,target,k,left+1)
            return left + 1
        if right>0:
            self.dfs(res,node.left,target,k,right+1)
            return right + 1
        
        return 0
          
        
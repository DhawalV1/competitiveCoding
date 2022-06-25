# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []
        return self.helper(1,n)
        
   
        
    def helper(self,s,e):
        if s>e:
            return [None]
        
        all_trees = []
        
        for cr in range(s,e+1):
            
            al_left = self.helper(s,cr-1)
            al_right = self.helper(cr+1,e)
            
            for left_t in al_left:
                for right_t in al_right:
                    
                    cro = TreeNode(cr)
                    cro.left = left_t
                    cro.right = right_t
                    
                    all_trees.append(cro)
        return all_trees
        
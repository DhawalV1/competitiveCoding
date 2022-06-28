# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        q = [(root,0,0)]
        left = cur = ans = 0
        for node,depth,pos in q:
            if node:
                q.append((node.left,depth+1,pos*2))
                q.append((node.right,depth+1,pos*2 + 1))
                
                if cur != depth:
                    cur = depth
                    left = pos
                    
                ans = max(pos-left+1,ans)
                
        return ans
        
        
        
        
       
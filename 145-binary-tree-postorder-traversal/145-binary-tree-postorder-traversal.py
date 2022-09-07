# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        p = [root]
        traver = []
        while p:
            node = p.pop()
            if node:
                traver.append(node.val)
                p.append(node.left)
                p.append(node.right)
            
        return traver[::-1] 
        
   
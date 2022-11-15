# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        h = self.height(root)
        nodes = 0
        while(root!=None):
            if self.height(root.right)==h-1:
                nodes += 1<<h
                root = root.right
            else:
                nodes +=  1<<(h-1)
                root = root.left
            h = h-1
            
        return nodes
        
    
    def height(self,root):
        if root is None:
            return -1
        else:
            return (self.height(root.left)+1)#self.countNodes1(root.right)+1)
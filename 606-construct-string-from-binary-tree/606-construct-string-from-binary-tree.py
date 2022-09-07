# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        out = []
        
        def _walk(node):
            out.append(str(node.val))
            
            if node.left:
                out.append('(')
                _walk(node.left)
                out.append(')')
                
            if not node.left and node.right:
                out.append('()')
                
            if node.right:
                out.append('(')
                _walk(node.right)
                out.append(')')
        
        _walk(root)
        return ''.join(out)
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        deque = []
        deque.append(root)
        
        ret = []
        while len(deque)>0:
            node = deque.pop()
            ret.append(node.val)
            
            
            if node.right is not None:
                deque.append(node.right)
            if node.left is not None:
                deque.append(node.left)
                
            
        return ret
            
        
        '''
        ret = []
        if root is None:
            return ret
        self.irder(root,ret)
        return ret
    def irder(self,root,ret):
        if root is None:
            return ret
        
        while(root):
            ret.append(root.val)
            self.irder(root.left,ret)
            self.irder(root.right,ret)
            
        '''
            
        
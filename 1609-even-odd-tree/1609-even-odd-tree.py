# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return 
        level = 0
        result = []
        queue = [root]
        
        while queue:
            prev = None
            length = len(queue)
            temp = []
            for i in range(length):
                node = queue.pop(0)
                if (level % 2 == 0 and (node.val % 2 == 0 or (prev is not None and node.val <= prev))) or \
                   (level % 2 == 1 and (node.val % 2 == 1 or (prev is not None and node.val >= prev))):
                    return False
                prev = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            level += 1
            
        return True
            
            
            
            
        
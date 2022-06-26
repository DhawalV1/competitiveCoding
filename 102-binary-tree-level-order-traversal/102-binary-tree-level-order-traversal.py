# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return 
        
        queue = []
        ans = []
        
        queue.append(root)
        ans = [[root.val]]
        
        while(len(queue)):
            size = len(queue)
            tmp = []
            while size:
            
                node = queue.pop(0)

                if node.left is not None:
                    queue.append(node.left)
                    tmp.append(node.left.val)

                if node.right is not None:
                    queue.append(node.right)
                    tmp.append(node.right.val)
                size -= 1
            
            if len(tmp):
                ans.append(tmp)
        return ans

        
                
                
        
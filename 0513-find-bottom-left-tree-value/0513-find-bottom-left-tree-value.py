# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        level = []
        value = []
        

    # Define a helper function for recursive traversal
        def traverse(node, depth):
            if node is None:
                return
            # Append depth and value of the current node
            
            level.append(depth)
            value.append(node.val)
            # Recursively traverse left and right subtrees with incremented depth
            traverse(node.left, depth + 1)
            traverse(node.right, depth + 1)
        traverse(root,0)
        
        return value[level.index(max(level))]

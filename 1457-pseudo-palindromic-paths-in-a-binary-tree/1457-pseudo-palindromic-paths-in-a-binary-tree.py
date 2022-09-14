# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        
        
        if not root: return 0
        
        
        def pseudofind(root,seen):
        
            if not root: return 0

            if root.val in seen:
                seen.remove(root.val)
            else:
                seen.add(root.val)
            if not root.left and not root.right:
                return 1 if len(seen) <= 1 else 0

            left = pseudofind(root.left,set(seen))
            right = pseudofind(root.right,set(seen))

            return left+right
        return pseudofind(root,set())

        
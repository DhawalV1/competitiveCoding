# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        '''
        if root is None:
            return 0
        if root.val >high:
            return self.rangeSumBST(root.left,low,high)
        if root.val<low:
            return self.rangeSumBST(root.right,low,high)
        return root.val + self.rangeSumBST(root.left,low,high) + self.rangeSumBST(root.right,low,high)
    
        '''
        
        if root is None:
            return 0
        elif root.val<(high+1) and root.val>(low-1):
            return root.val + self.rangeSumBST(root.left,low,high) + self.rangeSumBST(root.right,low,high)
        else:
            return self.rangeSumBST(root.left,low,high) + self.rangeSumBST(root.right,low,high)
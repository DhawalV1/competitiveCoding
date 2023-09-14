# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:return []
        q,ans =[root],[]
        while q:
            qlen = len(q)
            res1 = []
            
            for i in range(qlen):
                curr = q.pop(0)
                res1.append(curr.val)
                if curr.left: q.append(curr.left)
                if curr.right: q.append(curr.right)
            ans.append(res1)
            
        return ans[::-1]
            
        
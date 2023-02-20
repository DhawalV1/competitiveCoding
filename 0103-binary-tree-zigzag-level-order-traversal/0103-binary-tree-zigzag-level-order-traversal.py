# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        deque = collections.deque()
        if root:
            deque.append(root)
        res, level = [], 0
        while deque:
            l, size = [], len(deque)
            for _ in range(size): # process level by level
                node = deque.popleft()
                l.append(node.val)
                if node.left:
                    deque.append(node.left)
                if node.right:
                    deque.append(node.right)
            if level % 2 == 1:
                l.reverse()
            res.append(l)
            level += 1
        return res
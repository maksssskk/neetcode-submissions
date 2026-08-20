# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        level = []
        q = deque()
        q.append((root, root.val))
        while q:
            curr_l = []
            for _ in range(len(q)):
                node, val = q.popleft()
                curr_l.append(val)
                if node.left:
                    q.append((node.left, node.left.val))
                if node.right:
                    q.append((node.right, node.right.val))
            level.append(curr_l)
        return level

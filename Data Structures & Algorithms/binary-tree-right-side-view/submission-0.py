# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        level = []
        q = deque()
        q.append((root, root.val))
        while q:
            size = len(q)
            for i in range(size):
                node, val = q.popleft()
                if i == size - 1:
                    level.append(val)
                if node.left:
                    q.append((node.left, node.left.val))
                if node.right:
                    q.append((node.right, node.right.val))
        return level
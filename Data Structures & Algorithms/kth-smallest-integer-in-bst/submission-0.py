# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0
        q = deque()
        tree = []
        q.append((root, root.val))
        while q:
            root, val = q.popleft()
            tree.append(val)
            if root.left: q.append((root.left, root.left.val))
            if root.right: q.append((root.right, root.right.val))
        tree.sort()
        return tree[k - 1]    
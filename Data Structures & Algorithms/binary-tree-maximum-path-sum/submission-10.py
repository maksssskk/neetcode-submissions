# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_s = float('-inf')
        def sum_path(root):
            if not root:
                return 0

            l_max = max(0, sum_path(root.left))
            r_max = max(0, sum_path(root.right))
            self.max_s = max(self.max_s, root.val + l_max + r_max)
            
            return root.val + max(l_max, r_max)
        sum_path(root)
        return self.max_s

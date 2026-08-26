# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return 'N'
        res = []
        q = deque()
        q.append(root)
        while q:
            root = q.popleft()
            if root:
                q.append(root.left)
                q.append(root.right)
                res.append(str(root.val))
            else:
                res.append('N')
        return ','.join(res)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data or data[0].upper() == 'N':
            return None
        data = data.split(',')
        root = TreeNode(int(data[0]))
        i = 1
        q = deque()
        q.append(root)
        
        while q and i < len(data):
            n = q.popleft()
            if i < len(data) and data[i] != 'N':
                n.left = TreeNode(int(data[i]))
                q.append(n.left)
            i += 1
            if i < len(data) and data[i] != 'N':
                n.right = TreeNode(int(data[i]))
                q.append(n.right)
            i += 1
        return root
            

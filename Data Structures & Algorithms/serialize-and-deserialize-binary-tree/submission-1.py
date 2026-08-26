# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        q = deque([root])
        while q:
            n = q.popleft()
            if n:
                res.append(str(n.val))
                q.append(n.left)
                q.append(n.right)
            else:
                res.append('null')
        while res and res [-1] == 'null':
            res.pop()
        return ','.join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data:
            return TreeNode(data) 
        else:
            return None

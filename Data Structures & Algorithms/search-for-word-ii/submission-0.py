class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for w in words:
            trie.insert(w)

        res = set()
        h = len(board)
        w = len(board[0])
        def dfs(r, c, node):
            if r < 0 or r >= h or c < 0 or c >= w: 
                return
                
            el = board[r][c]
            if el not in node.children:
                return 
            next_node = node.children[el]
            if next_node.word:
                res.add(next_node.word)
                next_node.word = None

            temp = board[r][c]
            board[r][c] = '#'

            dfs(r-1, c, next_node)
            dfs(r+1, c, next_node)
            dfs(r, c-1, next_node)
            dfs(r, c+1, next_node)

            board[r][c] = temp
        for r in range(h):
            for c in range(w):
                dfs(r, c, trie.root)
        return list(res)
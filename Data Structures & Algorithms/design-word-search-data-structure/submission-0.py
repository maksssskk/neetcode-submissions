class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        d = self.trie
        for c in word:
            if c not in d:
                d[c] = {}
            d = d[c]
        d['#'] = '#'

    def search(self, word: str) -> bool:
        def sea(index, curr_d):
            if index == len(word):
                return '#' in curr_d
            
            c = word[index]
            if c == '.':
                for key in curr_d:
                    if key != '#':
                        if sea(index + 1, curr_d[key]):
                            return True
                return False
            if c in curr_d:
                return sea(index + 1, curr_d[c])
            return False
        return sea(0, self.trie)

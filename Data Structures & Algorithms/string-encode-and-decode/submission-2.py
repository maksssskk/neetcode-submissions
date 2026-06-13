class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ''
        for char in strs:
            result += (''.join(f'{len(char)}#{char}'))
        return result

    def decode(self, s: str) -> List[str]:
        words = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != '#':
                j += 1
            
            word_len = int(s[i:j])

            word = s[j+1:j+1+word_len]
            words.append(word)
            i = j + 1 + word_len

        return words
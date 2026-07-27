class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        h = [0] * 26
        max_s = 0
        max_len = 0

        for r in range(len(s)):
            char = s[r]
            h[ord(char) - ord('A')] += 1
            max_s = max(max_s,  h[ord(char) - ord('A')])
            if (r - l + 1) - max_s <= k:
                max_len = r - l + 1
                r += 1
            else:
                left_char = s[l]
                h[ord(left_char) - ord('A')] -= 1
                l += 1
                max_len = max(max_len, r - l + 1)
        return max_len
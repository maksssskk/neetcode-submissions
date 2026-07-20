class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        h = set()
        max_l = 0
        for r in range(len(s)):
            while s[r] in h:
                h.remove(s[l])
                l += 1
            h.add(s[r])
            max_l = max(max_l, r - l + 1)
        return max_l
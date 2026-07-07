class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == '':
            return ''

        countT = {}
        window = {}

        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have = 0
        need = len(countT)
        l = 0
        resLen = float("inf")
        res = [-1, -1]

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            if c in countT and countT[c] == window[c]:
                have += 1
            while have == need:
                currLen = r - l + 1
                if currLen < resLen:
                    resLen = currLen
                    res = [l, r]
                h = s[l]
                window[h] -= 1
                if h in countT and countT[h] > window[h]:
                    have -= 1
                l += 1
        if resLen != float('inf'):
            return s[res[0] : res[1] + 1]
        else:
            return ''


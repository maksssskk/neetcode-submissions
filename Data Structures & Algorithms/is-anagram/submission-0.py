class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        set_s = set(s)

        if len(s) != len(t):
            return False
            
        for char in set_s:
            if s.count(char) != t.count(char):
                return False
        return True

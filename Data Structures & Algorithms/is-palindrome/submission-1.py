import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(s.split())

        s = s.translate(str.maketrans("", "", string.punctuation))

        if s.lower() == s.lower()[::-1]:
            return True
        else:
            return False
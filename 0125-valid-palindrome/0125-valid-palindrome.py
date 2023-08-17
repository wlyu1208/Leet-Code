import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower = s.lower()
        chars = re.sub(r'[^a-z0-9]', '',lower)

        if chars == chars[::-1]:
            return True

        return False
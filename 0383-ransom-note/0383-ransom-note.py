from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r = Counter(ransomNote)
        m = Counter(magazine)

        for c in r:
            if c not in m:
                return False
            if r[c] > m[c]:
                return False
        return True
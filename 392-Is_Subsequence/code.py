class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0 and len(t) > 0:
            return True
        
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        if i != len(s):
            return False
        
        return True

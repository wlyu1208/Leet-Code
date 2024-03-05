class Solution:
    def minimumLength(self, s: str) -> int:
        i, j = 0, len(s) -1

        while i < j and s[i] == s[j]:
            idx = s[i]

            while i <= j and s[i] == idx:
                i += 1
            
            while i <= j and s[j] == idx:
                j -= 1
        return j - i + 1
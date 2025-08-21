class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len_n = len(needle)
        len_h = len(haystack)
        if len_n > len_h:
            return -1

        for i in range(len_h):
            if i + len_n > len_h:
                break
            sub_h = haystack[i:i+len_n]
            if sub_h == needle:
                return i
        return -1
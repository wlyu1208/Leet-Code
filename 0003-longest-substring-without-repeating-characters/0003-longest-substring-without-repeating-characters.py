from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = defaultdict()
        l = 0
        _max = 0
        
        for r in range(len(s)):
            c = s[r]

            if c in seen and seen[c] >= l:
                l = seen[c] + 1
            else:
                _max = max(_max, r - l + 1)
            seen[c] = r
        return _max
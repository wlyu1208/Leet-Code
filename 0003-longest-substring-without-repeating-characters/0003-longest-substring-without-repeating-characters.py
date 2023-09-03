from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        seen = defaultdict()
        n = len(s)
        ans = 0
        for r in range(n):
            c = s[r]

            if c in seen and seen[c] >= l:
                l = seen[c] + 1
            else:
                ans = max(ans, r - l + 1)
            seen[c] = r

        return ans


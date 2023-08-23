from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnt = Counter(s)
        has_odd = False
        twos = 0

        for i in cnt:
            if cnt[i] % 2:
                has_odd = True
            if cnt[i] >= 2:
                twos += int(cnt[i] / 2)

        return 2*twos + 1 if has_odd else 2*twos
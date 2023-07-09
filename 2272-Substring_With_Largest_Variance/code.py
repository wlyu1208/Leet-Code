class Solution:
    def largestVariance(self, s: str) -> int:
        ans = 0
        for a, b in permutations(set(s), 2):
            cnt = 0
            hasB = firstB = False
            for c in s:
                if c == a:
                    cnt += 1
                if c == b:
                    hasB = True
                    if firstB and cnt >= 0:
                        firstB = False
                    else:
                        cnt -= 1
                        if cnt < 0:
                            firstB = True
                            cnt = -1
                if hasB and cnt > ans:
                    ans = cnt
        return ans

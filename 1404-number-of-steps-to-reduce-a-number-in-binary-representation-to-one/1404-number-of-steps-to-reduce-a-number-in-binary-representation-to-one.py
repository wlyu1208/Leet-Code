class Solution:
    def numSteps(self, s: str) -> int:
        _int = int(s, 2)
        if _int <= 1:
            return 0

        cnt = 0
        while _int > 1:
            #odd
            if _int % 2:
                _int += 1
            else:
                _int //= 2
            cnt += 1

        return cnt
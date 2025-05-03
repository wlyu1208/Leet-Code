class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        _min = 2 * (10 ** 5)

        for i in range(1, 7):
            t_swap, b_swap = 0, 0
            valid = True
            for t, b in zip(tops, bottoms):
                if i != t and i != b:
                    valid = False
                    break
                if i != t:
                    t_swap += 1
                if i != b:
                    b_swap += 1
            if valid:
                _min = min(_min, t_swap, b_swap)
        return -1 if _min == 2 * (10 ** 5) else _min
                
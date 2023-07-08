class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if len(weights) == 1:
            return 0
        _sum = list()

        for x, y in zip(weights, weights[1:]):
            _sum.append(x + y)
        
        _sum.sort()

        mn = _sum[0] + _sum[-1]
        mx = copy.deepcopy(mn)
        
        for i in range(k-1):
            mn += _sum[i]
            mx += _sum[len(_sum)-i-1]
        
        return mx - mn

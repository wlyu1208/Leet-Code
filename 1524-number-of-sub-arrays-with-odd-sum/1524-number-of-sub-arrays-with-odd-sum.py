class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        _mod = 10**9 + 7
        _odd, _even = 0, 1
        prefix = 0
        result = 0
        for n in arr:
            prefix += n

            # even
            if prefix % 2 == 0:
                result += _odd
                _even += 1
            # odd
            else:
                result += _even
                _odd += 1
        result %= _mod
        return result
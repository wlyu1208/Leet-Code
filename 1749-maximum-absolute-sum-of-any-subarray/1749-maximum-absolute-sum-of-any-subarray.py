class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        _sum, _max, _min = 0, 0, 0

        for n in nums:
            _sum += n
            _max = max(_sum, _max)
            _min = min(_sum, _min)

        return abs(_max - _min)
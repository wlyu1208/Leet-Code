class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        _sum = sum(nums)
        if _sum % 2: return False
        target = _sum // 2
        n = len(nums)

        _set = set()
        _set.add(0)
        _set.add(nums[-1])

        for i in reversed(range(n-1)):
            _new_set = set()
            for x in _set:
                _new_set.add(x)
                _new_set.add(x + nums[i])
            _set = _new_set
        return True if target in _set else False
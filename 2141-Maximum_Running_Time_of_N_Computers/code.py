class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        _sum = sum(batteries)

        batteries.sort()

        while batteries[-1] > _sum // n:
            _sum -= batteries.pop()
            n -= 1
        
        return _sum // n

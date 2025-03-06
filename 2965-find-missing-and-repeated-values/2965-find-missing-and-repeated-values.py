class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        counter = Counter()
        n = len(grid)
        _pool = [i+1 for i in range(n*n)]
        for _list in grid:
            counter += Counter(_list)

        a = 0
        for i in _pool:
            if i not in counter.keys():
                a = i
        for k, v in counter.items():
            if v == 2:
                return [k, a]
        return [0, 0]
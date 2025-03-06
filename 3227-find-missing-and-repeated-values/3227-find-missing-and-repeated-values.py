class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        size = n * n
        _map = [0] * (size + 1)
        repeated, missing = -1, -1

        for row in grid:
            for value in row:
                _map[value] += 1
        
        for num in range(1, size+1):
            if _map[num] == 2:
                repeated = num
            elif _map[num] == 0:
                missing = num
        return repeated, missing
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rev_grid = list(map(list, zip(*grid)))
        n = len(grid)
        cnt = 0

        for i in range(n):
            for j in range(n):
                if grid[i] == rev_grid[j]:
                    cnt += 1

        return cnt

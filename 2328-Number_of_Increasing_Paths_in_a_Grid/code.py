class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        mod = 10**9 + 7
        
        # r, l, u, d
        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]

        total = 0

        @cache
        def go(r, c):
            total = 1
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] > grid[r][c]:
                    total += go(nr, nc)
            
            return total

        for i in range(m):
            for j in range(n):
                total += go(i, j)
        
        return total % mod

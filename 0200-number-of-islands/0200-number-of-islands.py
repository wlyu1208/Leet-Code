class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        def mark(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == '0':
                return
            
            grid[r][c] = '0'
            mark(r + 1, c)
            mark(r - 1, c)
            mark(r, c + 1)
            mark(r, c - 1)

        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    mark(i, j)
                    cnt += 1
                
        return cnt
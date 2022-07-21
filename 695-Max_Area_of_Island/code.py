class Solution:
    def dfs(self, grid, r, c, m, n):
        if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0:
            return 0
        
        grid[r][c] = 0
        
        return 1 + self.dfs(grid, r + 1, c, m, n) + self.dfs(grid, r - 1, c, m, n) + self.dfs(grid, r, c + 1, m, n) + self.dfs(grid, r, c - 1, m, n)
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        areas = []
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    areas.append(self.dfs(grid, r, c, m, n))
        if len(areas) == 0:
            return 0
        else:
            return max(areas)

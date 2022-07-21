class Solution:
    def get_nei(self, grid, n_r, n_c, m, n):
        if n_r < 0 or n_r >= m or n_c < 0 or n_c >= n or grid[n_r][n_c] == 0:
            return 0
        else:
            return 1
        
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        answer = 0
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    neis = 0
                    for d in dirs:
                        neis += self.get_nei(grid, r + d[0], c + d[1], m, n)
                    answer += 4 - neis
        
        return answer

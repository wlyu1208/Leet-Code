class Solution:
    def dfs(self, grid, cur_i, cur_j, m, n):
        if cur_i < 0 or cur_i >= m or cur_j < 0 or cur_j >= n or grid[cur_i][cur_j] == 0:
            return
        
        grid[cur_i][cur_j] = 0
        self.dfs(grid, cur_i-1, cur_j, m, n)
        self.dfs(grid, cur_i+1, cur_j, m, n)
        self.dfs(grid, cur_i, cur_j-1, m, n)
        self.dfs(grid, cur_i, cur_j+1, m, n)


        
    
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
    
        answer = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    self.dfs(grid, i, j, m, n)
                    answer += 1
        return answer

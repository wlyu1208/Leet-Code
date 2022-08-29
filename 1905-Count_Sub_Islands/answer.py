class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        r, c = len(grid1), len(grid1[0])
        
        def dfs(i, j):
            if i < 0 or i >= r or j < 0 or j >= c:
                return 1
            
            if grid2[i][j] == 0:
                return 1
            
            grid2[i][j] = 0
            
            return dfs(i-1, j) & dfs(i+1, j) & dfs(i, j-1) & dfs(i, j+1) & grid1[i][j]
        
        answer = 0
        for cur_r in range(r):
            for cur_c in range(c):
                if grid2[cur_r][cur_c] == 1:
                    answer += dfs(cur_r, cur_c)
        
        return answer

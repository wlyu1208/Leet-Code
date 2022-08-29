# RUN TIME ERROR
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def find_island(cur_r, cur_c, grid, r, c, cur_island):
            if cur_r < 0 or cur_r >= r or cur_c < 0 or cur_c >= c:
                return

            if grid[cur_r][cur_c] == 0:
                return


            grid[cur_r][cur_c] = 0
            find_island(cur_r - 1, cur_c, grid, r, c, cur_island)
            find_island(cur_r + 1, cur_c, grid, r, c, cur_island)
            find_island(cur_r, cur_c - 1, grid, r, c, cur_island)
            find_island(cur_r, cur_c + 1, grid, r, c, cur_island)

            cur_island.append((cur_r, cur_c))

        r1, c1, r2, c2 = len(grid1), len(grid1[0]), len(grid2), len(grid2[0])

        islands1 = []
        for r in range(r1):
            for c in range(c1):
                cur_island = []
                if grid1[r][c] == 1:
                    find_island(r, c, grid1, r1, c1, cur_island)
                    islands1.append(cur_island)

        islands2 = []
        for r in range(r2):
            for c in range(c2):
                cur_island = []
                if grid2[r][c] == 1:
                    find_island(r, c, grid2, r2, c2, cur_island)
                    islands2.append(cur_island)

        answer = 0
        for cur2 in islands2:
            for cur1 in islands1:
                if len(cur2) <= len(cur1):
                    if all(item in cur1 for item in cur2):
                        answer += 1
        return answer

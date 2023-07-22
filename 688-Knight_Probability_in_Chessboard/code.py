class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        if k == 0:
            return 1
        
        max_moves = 8 ** k

        moves = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (-2, 1), (2, -1), (-2, -1)]

        @cache
        def dfs(r, c, cnt):
            if r < 0 or r >= n or c < 0 or c >= n:
                return 0
            if cnt == k:
                return 1
            result = 0
            for dr, dc in moves:
                nr, nc = r + dr, c + dc
                result += dfs(nr, nc, cnt + 1)
            return result
        
        possible_moves = dfs(row, column, 0)

        return float(possible_moves / max_moves)

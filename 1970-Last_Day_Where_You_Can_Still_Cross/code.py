class Solution:
    def possible(self, mid, m, n, cells):
        grid = [[0]*n for _ in range(m)]

        for i in range(mid):
            r, c = cells[i]
            grid[r-1][c-1] = 1
        visit = set()

        stack = [(0, c) for c in range(n) if grid[0][c] == 0]
        while stack:
            r, c = stack.pop()
            if r == m - 1:
                return True
            if (r, c) in visit:
                continue
            visit.add((r,c))
            for dr, dc in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                nr, nc = r+dr, c+dc

                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 0:
                    stack.append((nr, nc))
        return False

    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        l, r = 0, len(cells)

        ans = -1

        while l <= r:
            mid = (r + l) // 2

            if self.possible(mid, row, col, cells):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1

        return ans

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        original = image[sr][sc]

        q = [(sr, sc)]
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visit = set()

        while q:
            r, c =  q.pop()
            image[r][c] = color
            visit.add((r, c))

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n and image[nr][nc] == original and (nr, nc) not in visit:
                    q.append((nr, nc))

        return image
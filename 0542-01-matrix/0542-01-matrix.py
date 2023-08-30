class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])

        MAX_VAL = float('inf')

        q = []

        for i in range(m):
            for j in range(n):
                if mat[i][j]:
                    mat[i][j] = MAX_VAL
                else:
                    q.append((i, j))
        
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while q:
            r, c = q.pop(0)

            for d in dirs:
                n_r, n_c = r + d[0], c + d[1]

                if 0 <= n_r < m and 0 <= n_c < n and mat[n_r][n_c] > mat[r][c] + 1:
                    mat[n_r][n_c] = mat[r][c] + 1
                    q.append((n_r, n_c))
        
        return mat
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])

        def check_lucky(r, c, val):
            row = matrix[r]
            
            col, current_r = [], 0
            while current_r < m:
                col.append(matrix[current_r][c])
                current_r += 1

            return (min(row) == val) and (max(col) == val)

        res = []
        for i in range(m):
            for j in range(n):
                if check_lucky(i, j, matrix[i][j]):
                    res.append(matrix[i][j])
        
        return res
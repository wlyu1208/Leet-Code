class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        h_s = [[0]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    h_s[i][j] = h_s[i-1][j] + 1 if i > 0 else 1
    
        answer = 0
        for i in range(m):
            for j in range(n):
                if h_s[i][j] > 0:
                    min_h = h_s[i][j]
                    for k in range(j, -1, -1):
                        if h_s[i][k] == 0:
                            break
                        min_h = min(min_h, h_s[i][k])
                        answer += min_h
        return answer
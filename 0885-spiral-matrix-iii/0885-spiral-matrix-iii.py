class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        step = 1
        total = rows * cols
        ans = []
        r, c = rStart, cStart
        d = 0

        while len(ans) < total:
            for _ in range(2):
                for _ in range(step):
                    if 0<=r<rows and 0<=c<cols:
                        ans.append((r, c))
                    if len(ans) == total:
                        return ans
                    
                    r += dirs[d][0]
                    c += dirs[d][1]
                d = (d+1)%4
            step += 1
        
        return ans
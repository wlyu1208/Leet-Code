import math
class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_diag = float('-inf')
        answer = -1
        for a, b in dimensions:
            now_diag = a * a + b * b
            if now_diag > max_diag:
                answer = a * b
                max_diag = now_diag
            elif now_diag == max_diag and a*b >= answer:
                answer = a * b
        return answer
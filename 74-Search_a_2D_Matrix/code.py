class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        r, c = m - 1, 0

        while r >= 0 and c < n:
            current =  matrix[r][c]

            if current == target:
                return True
            elif current > target:
                r -= 1
            else:
                c += 1
    
        return False

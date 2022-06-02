class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row_len = len(matrix)
        col_len = len(matrix[0])
        answer = [ [0]* row_len for x in range(col_len)] 
        for i in range(row_len):
            for j in range(col_len):
                answer[j][i] = matrix[i][j]
        
        return answer

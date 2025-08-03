class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        answer = []

        for i in range(numRows):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = answer[i-1][j-1] + answer[i-1][j]
            answer.append(row)
        
        return answer
class Solution:
    def iterate(self, last_list):
        next_list = [1]
        n = len(last_list)
        for j in range(1, n):
            next_list.append(last_list[j]+last_list[j-1])
        next_list.append(1)
        return next_list
        
    def generate(self, numRows: int) -> List[List[int]]:
        answer = [[1]]
        
        for _ in range(numRows-1):
            answer.append(self.iterate(answer[-1]))
        
        return answer

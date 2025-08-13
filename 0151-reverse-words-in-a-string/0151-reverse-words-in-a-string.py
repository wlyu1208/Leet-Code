class Solution:
    def reverseWords(self, s: str) -> str:
        x = s.split(' ')
        
        answer = []
        for i in range(len(x)-1, -1, -1):
            if x[i] != '':
                answer.append(x[i])
        
        return ' '.join(answer)
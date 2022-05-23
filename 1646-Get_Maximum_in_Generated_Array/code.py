class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        
        answer = [0, 1]
        max_num = -1
        for i in range(2, n + 1):
            if i % 2 == 0:
                x = answer[i // 2]
                if x > max_num:
                    max_num = x
                answer.append(x)
            else: 
                x = answer[(i // 2)] + answer[(i // 2) + 1]
                if x > max_num:
                    max_num = x
                answer.append(x)
        
        return max_num

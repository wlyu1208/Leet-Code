from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = ['+', '-', '*', '/']
        q = deque([])
        for i in tokens:
            if i in ops:
                n1 = q.pop()
                n2 = q.pop()
                if i == ops[0]:
                    q.append(n1 + n2)
                elif i == ops[1]:
                    q.append(n2 - n1)
                elif i == ops[2]:
                    q.append(n1 * n2)
                elif i == ops[3]:
                    q.append(int(n2 / n1))
            else:
                q.append(int(i))
        return q.pop()
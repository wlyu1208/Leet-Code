class Solution:
    def largestGoodInteger(self, num: str) -> str:
        current = ''
        answer = ''
        _max = 0

        for c in str(num):
            if current == '':
                current += c
                continue
            
            if current[-1] != c:
                current = c
                continue
            
            current += c
            if len(current) == 3:
                if answer == '':
                    answer = current
                    _max = int(current)
                else:
                    if int(current) > _max:
                        _max = int(current)
                        answer = current
        return answer
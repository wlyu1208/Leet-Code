class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        answer = []
        current = []
        for i in range(len(s)):
            current.append(s[i])

            if len(current) == k:
                answer.append(''.join(current))
                current = []
        
        if current:
            while len(current) < k:
                current.append(fill)
            answer.append(''.join(current))
        
        return answer
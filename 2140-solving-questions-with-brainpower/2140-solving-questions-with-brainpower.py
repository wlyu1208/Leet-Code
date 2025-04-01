class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        cache = [0] * (n+1)
        for i in reversed(range(n)):
            pt, bp = questions[i]
            
            next_i = i + 1 + bp
            solve = pt + (cache[next_i] if next_i < n else 0)
            skip = cache[i+1] if i < n else 0
            cache[i] = max(solve, skip)

        return cache[0]


        n = len(questions)
        cache = [0] * n

        def find_max(i):
            if i >= n:
                return 0

            if cache[i] != 0:
                return cache[i]
            
            point, brain_power = questions[i]

            cache[i] = max(
                find_max(i+1),
                point + find_max(i + 1 + brain_power)
            )
            return cache[i]
        
        return find_max(0)
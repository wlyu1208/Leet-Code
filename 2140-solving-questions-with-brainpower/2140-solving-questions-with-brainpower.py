class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)

        def find_max(i):
            if i >= n:
                return 0
            
            point, brain_power = questions[i]

            return max(
                find_max(i+1),
                point + find_max(i + 1 + brain_power)
            )
        
        return find_max(0)
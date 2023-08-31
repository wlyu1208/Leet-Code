class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(x, y):
            return math.sqrt(x**2 + y**2)

        temp = []

        for x, y in points:
            temp.append((dist(x, y), x, y))
        
        sorted_temp = sorted(temp, key=lambda x: x[0])
        
        answer = []
        for i in range(k):
            answer.append((sorted_temp[i][1], sorted_temp[i][2]))

        return answer
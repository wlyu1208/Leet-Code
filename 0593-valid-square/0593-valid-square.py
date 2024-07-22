class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def dist(point1, point2):
            return math.sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)
        
        ps = [p1, p2, p3, p4]
        dist_set = set(
            [dist(x, y) for x, y in itertools.combinations(ps, 2)]
        )
        if 0 in dist_set:
            return False
        
        return len(dist_set) == 2
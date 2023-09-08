class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        req_map = defaultdict(list)

        for a, b in prerequisites:
            req_map[a].append(b)
        

        visit = set()
        def dfs(course):
            if not req_map[course]:
                return True    
            if course in visit:
                return False
                
            visit.add(course)

            for p in req_map[course]:
                if not dfs(p): return False
                
            req_map[course] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
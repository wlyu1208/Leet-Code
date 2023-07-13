class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = collections.defaultdict(list)

        for course, pre in prerequisites:
            edges[pre].append(course)
        
        def cycle(current, keep_track, visited):
            keep_track[current] = True
            visited[current] = True
            for i in edges[current]:
                if i not in visit and cycle(i, keep_track, visited):
                    return True
                elif i in keep_track:
                    return True
            keep_track.pop(current)
            return False

        visit = dict()
        for n in range(numCourses):
            track = dict()
            if n not in visit and cycle(n, track, visit):
                return False

        return True

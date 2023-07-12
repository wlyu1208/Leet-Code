class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)

        safe = {}

        def dfs(i):
            if i in safe:
                return safe[i]
            safe[i] = False
            for _next in graph[i]:
                if not dfs(_next):
                    return safe[i]
            safe[i] = True
            return safe[i]

        ans = list()
        for i in range(n):
            if dfs(i):
                ans.append(i)
        return ans


# need to study https://www.youtube.com/watch?v=Re_v0j0CRsg

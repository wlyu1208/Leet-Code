class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        _dict = defaultdict(list)

        for u, v in edges:
            _dict[u].append(v)
            _dict[v].append(u)
        
        def dfs(node, visit):
            if node == destination:
                return True
            
            visit.add(node)
            for _next in _dict[node]:
                if _next not in visit and dfs(_next, visit):
                    return True
            return False
        
        visit = set()
        return dfs(source, visit)
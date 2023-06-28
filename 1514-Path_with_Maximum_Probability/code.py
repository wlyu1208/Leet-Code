class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        adj = collections.defaultdict(list)

        for (u, v), p in zip(edges, succProb):
            adj[u].append((v, p))
            adj[v].append((u, p))

        heap = [(-1.0, start)]
        visit = set()

        while heap:
            dist, node = heapq.heappop(heap)
            visit.add(node)

            if node == end:
                return dist * -1
            
            for _next, prob in adj[node]:
                if _next not in visit:
                    heapq.heappush(heap, (dist * prob, _next))
        
        return 0

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        probs = [0] * n
        probs[start_node] = 1

        for _ in range(n-1):
            update = False
            for (u, v), z in zip(edges, succProb):
                if probs[u] * z > probs[v]:
                    probs[v] = probs[u] * z
                    update = True
                if probs[v] * z > probs[u]:
                    probs[u] = probs[v] * z
                    update = True
            if not update:
                break
        
        return probs[end_node]
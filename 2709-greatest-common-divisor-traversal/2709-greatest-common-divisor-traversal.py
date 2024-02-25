import math

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        _max = max(nums)

        _map = [[]for _ in range(_max+1)]
        for i, num in enumerate(nums):
            _map[num].append(i)
        
        _graph = defaultdict(list)

        for d in range(2, _max + 1):
            seq = chain.from_iterable(_map[m] for m in range(d, _max+1, d))
            for i, j in pairwise(seq):
                _graph[i].append(j)
                _graph[j].append(i)
        
        seen = [False] * len(nums)

        def dfs(v: int) -> None:
            seen[v] = True
            for u in _graph[v]:
                if not seen[u]:
                    dfs(u)
        dfs(0)

        return all(seen)



class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)

        MOD = 10**9 + 7
        has_cache = [[False] * (fuel+1) for _ in range(n)]
        cache = [[None] * (fuel+1) for _ in range(n)]

        def count(current, fuel):
            if fuel < 0:
                return 0
            
            if has_cache[current][fuel]:
                return cache[current][fuel]

            total = 0

            if current == finish:
                total += 1

            for i in range(n):
                if i == current:
                    continue
                
                cost = abs(locations[i] - locations[current])
                total += count(i, fuel - cost)
            
            has_cache[current][fuel] = True
            cache[current][fuel] = total

            return total
        result = count(start, fuel)
        return result % MOD

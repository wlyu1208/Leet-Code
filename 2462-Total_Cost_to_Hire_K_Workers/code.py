class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        h = list()
        n = len(costs)
        l = candidates
        r = n - candidates

        for i in range(l):
            heapq.heappush(h, (costs[i], i, 1))
        
        for i in range(max(r, l), n):
            heapq.heappush(h, (costs[i], i, -1))
        
        r -= 1

        ans = 0

        for _ in range(k):
            cost, idx, _dir = heapq.heappop(h)
            ans += cost

            if l <= r:
                if _dir == 1:
                    heapq.heappush(h, (costs[l], l, 1))
                    l += 1
                else:
                    heapq.heappush(h, (costs[r], r, -1))
                    r -= 1
        
        return ans

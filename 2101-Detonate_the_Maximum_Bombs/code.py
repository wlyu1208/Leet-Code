class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        track = [[] for _ in range(n)]
        for i in range(n):
            x, y, r = bombs[i]
            for j in range(n):
                if i == j: 
                    continue
                o_x, o_y, o_r = bombs[j]

                dx = x - o_x
                dy = y - o_y

                if dx ** 2 + dy ** 2 <= r ** 2:
                    track[i].append(j)
        
        result = 1

        for i in range(n):
            q = []
            q.append(i)
            visit = [0] * n
            visit[i] = 1

            while len(q) > 0:
                cur = q.pop(0)
                for nxt in track[cur]:
                    if visit[nxt]:
                        continue
                    q.append(nxt)
                    visit[nxt] = 1
            result = max(result, sum(visit))
        
        return result

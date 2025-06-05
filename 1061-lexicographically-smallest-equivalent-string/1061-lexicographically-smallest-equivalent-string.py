class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        adj = defaultdict(list)

        for a, b in zip(s1, s2):
            adj[a].append(b)
            adj[b].append(a)
        
        
        answer = list()

        def dfs(ch, visit):
            visit.add(ch)
            min_ch = ch

            for nei in adj[ch]:
                if nei not in visit:
                    rest = dfs(nei, visit)
                    min_ch = min(min_ch, rest)
            return min_ch

        for ch in baseStr:
            visit = set()
            answer.append(dfs(ch, visit))
        
        return ''.join(answer)
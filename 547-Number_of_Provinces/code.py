class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(x):
            visit.add(x)
            for j in range(n):
                if j not in visit and isConnected[x][j]:
                    dfs(j)

        n = len(isConnected)

        visit = set()
        province = 0

        for i in range(n):
            if i not in visit:
                dfs(i)
                province += 1
        
        return province

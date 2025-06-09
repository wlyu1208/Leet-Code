class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []

        def dfs(i):
            if i > n:
                return
            cur = i
            result.append(i)
            for i in range(10):
                tmp = str(cur) + str(i)
                dfs(int(tmp))

        for i in range(1, 10):
            dfs(i)
        
        return result
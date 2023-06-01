class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        from queue  import Queue
        n = len(grid)

        q = Queue()
        visit = set()

        if n == 1 and grid[0][0] == 0:
            return 1

        if grid[0][0] == 0:
            q.put((1, (0, 0)))
            visit.add((0,0))
        
        _dir = [-1, 0, 1]

        while not q.empty():
            dist, (r, c) = q.get()
            
            for dr in _dir:
                for dc in _dir:
                    new_r = r + dr
                    new_c = c + dc

                    if not ( 0 <= new_r < n):
                        continue
                    if not ( 0 <= new_c < n):
                        continue
                    if grid[new_r][new_c] == 1:
                        continue
                    if (new_r, new_c) in visit:
                        continue
                    
                    if new_r == n-1 and new_c == n-1:
                        return dist + 1
                    
                    q.put((dist+1, (new_r, new_c)))
                    visit.add((new_r, new_c))
        
        return -1

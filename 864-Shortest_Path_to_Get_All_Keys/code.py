class Solution:
  def shortestPathAllKeys(self, grid):
    m, n = len(grid), len(grid[0])
    all_keys = 0
    seen = [[[None]* 64 for _ in range(n)] for _ in range(m)]
    q = collections.deque()
    for i in range(m):
      for j in range(n):
        c = grid[i][j]
        if c == '@':
          q.append((j << 16) | (i << 8))
          seen[i][j][0] = 1
        elif c >= 'a' and c <= 'f':
          all_keys |= (1 << (ord(c) - ord('a')))
          
    dirs = [-1, 0, 1, 0, -1]
    steps = 0
    while q:
      size = len(q)
      while size > 0:
        size -= 1
        s = q.popleft()
        x = s >> 16
        y = (s >> 8) & 0xff
        keys = s & 0xff        
        if keys == all_keys: return steps
        for i in range(4):
          nx, ny, nkeys = x + dirs[i], y + dirs[i + 1], keys          
          if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
          c = grid[ny][nx]
          if c == '#': continue
          if c in string.ascii_uppercase and keys & (1 << (ord(c) - ord('A'))) == 0: continue
          if c in string.ascii_lowercase: nkeys |= (1 << (ord(c) - ord('a')))
          if seen[ny][nx][nkeys]: continue
          q.append((nx << 16) | (ny << 8) | nkeys)
          seen[ny][nx][nkeys] = 1
      steps += 1
    return -1

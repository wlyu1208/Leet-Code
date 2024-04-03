class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])
        visit = set()

        def find(r, c, cnt):
            if cnt == len(word):
                return True
            
            if r < 0 or r >= row or c < 0 or c >= col:
                return False
            
            if (r,c) in visit or board[r][c] != word[cnt]:
                return False
            
            visit.add((r, c))

            if (find(r+1, c, cnt+1) or find(r, c+1, cnt+1) or find(r-1, c, cnt+1) or find(r, c-1, cnt+1)):
                print(r, c, cnt)
                return True
            
            visit.remove((r, c))
            return False

        for r in range(row):
            for c in range(col):
                if find(r, c, 0): return True
        
        return False
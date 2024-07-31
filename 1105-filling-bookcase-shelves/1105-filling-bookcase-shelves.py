class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)


        @lru_cache(None)
        def find(idx, cur_h, w_left):
            if idx == n: return cur_h

            w, h = books[idx][0], books[idx][1]

            # next
            res = find(idx+1, h, shelfWidth-w) + cur_h

            # current
            if w <= w_left:
                res = min(res, find(idx+1, max(cur_h, h), w_left-w))

            return res


        return find(0, 0, shelfWidth)
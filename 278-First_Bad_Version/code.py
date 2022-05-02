class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 1
        end = n
        
        while True:
            pivot = (start + end) // 2
            
            cur = isBadVersion(pivot)

            if not cur:
                start = pivot + 1
            else:
                if pivot == 1:
                    return 1
                else:
                    prev = isBadVersion(pivot - 1)
                    if not prev:
                        return pivot
                    else:
                        end = pivot - 1

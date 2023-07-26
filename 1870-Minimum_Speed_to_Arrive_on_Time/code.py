class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        '''
        speed = distance / time(hour)
        1 <= distance <= 10**5
        1 <= time <= 10**9
        '''
        def can_make(speed):
            time = 0
            for d in dist:
                time = math.ceil(time)
                time += d / speed
            return True if time <= hour else False

        ans = float('inf')

        l, r = 1, 10**10

        while l <= r:
            mid = (l + r) // 2

            if can_make(mid):
                ans = min(ans, mid)
                r = mid - 1
            else:
                l = mid + 1
        return ans if ans != float('inf') else -1

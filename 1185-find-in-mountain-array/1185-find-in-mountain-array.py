# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()
        l, r = 0, n - 1

        while l < r:
            mid = (l + r) // 2

            mid_val = mountain_arr.get(mid)
            
            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                l = mid + 1
            else:
                r = mid
        
        peak = l

        l, r = 0, peak

        while l <= r:
            mid = (l + r) // 2

            mid_val = mountain_arr.get(mid)

            if mid_val == target:
                return mid
            elif mid_val < target:
                l = mid + 1
            else:
                r = mid - 1
        
        l, r = peak, n - 1

        while l <= r:
            mid = (l + r) // 2

            mid_val = mountain_arr.get(mid)

            if mid_val == target:
                return mid
            elif mid_val > target:
                l = mid + 1
            else:
                r = mid - 1

        return -1        

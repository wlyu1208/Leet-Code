class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2.sort()

        def find(val):
            result = float("inf")
            l, r = 0, len(arr2)-1
            while l <= r:
                piv = (l + r) // 2
                if arr2[piv] > val:
                    result = min(result, arr2[piv])
                    r = piv -1
                else:
                    l = piv + 1
            return result if result != float("inf") else -1

        visit = dict()
        def dp(idx, prev):
            if idx == len(arr1):
                return 0
            
            if (idx, prev) in visit:
                return visit[(idx, prev)]

            result = float("inf")
            if arr1[idx] > prev:
                result = min(result, dp(idx+1, arr1[idx]))
            
            greater = find(prev)
            if greater != -1:
                result = min(result, 1+dp(idx+1, greater))
            visit[(idx, prev)] = result
            return result

        result = dp(0, -1)
        return result if result != float("inf") else -1

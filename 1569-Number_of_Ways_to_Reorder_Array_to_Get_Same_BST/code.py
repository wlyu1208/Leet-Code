class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        mod = 10 ** 9 + 7

        factorial = [1] * len(nums)

        for i in range(1, len(nums)):
            factorial[i] = factorial[i-1] * i
        
        def combination(nl, nr):
            return factorial[nl+nr] // factorial[nl] // factorial[nr]

        def ways(arr):
            if len(arr) <= 2:
                return 1
            
            root = arr[0]
            l = [x for x in arr if x < root]
            r = [x for x in arr if x > root]

            return ways(l) * ways(r) * combination(len(l), len(r))
        
        return (ways(nums) - 1) % mod

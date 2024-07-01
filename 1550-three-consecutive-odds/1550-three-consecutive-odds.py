class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False

        _sum = (arr[0]%2) + (arr[1]%2) + (arr[2]%2)
        if _sum == 3: return True

        for i in range(3, len(arr)):
            _sum -= arr[i-3]%2
            _sum += arr[i] % 2

            if _sum == 3:
                return True
        
        return False
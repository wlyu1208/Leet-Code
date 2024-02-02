class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        _map = "123456789"
        _len = len(_map)

        for i in range(_len):
            for j in range(i+1, _len):
                num = int(_map[i:j+1])

                if num > high:
                    break
                if low <= num <= high:
                    ans.append(num)
        ans.sort()
        return ans

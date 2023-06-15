class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()

        x = arr[1] - arr[0]

        answer = True

        for i in range(len(arr)-1):
            if arr[i+1] - arr[i] != x:
                return False

        return True

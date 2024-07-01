class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        temp = []
        for num in arr:
            if num % 2:
                temp.append(num)
            else:
                temp = []
            
            if len(temp) == 3:
                return True

        return False
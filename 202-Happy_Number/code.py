class Solution:
    def isHappy(self, n: int) -> bool:
        track = set()
        while n != 1:
            if n in track:
                return False
            else:
                track.add(n)
                digits = list(str(n))
                n = sum(int(x) ** 2 for x in digits)
        return True

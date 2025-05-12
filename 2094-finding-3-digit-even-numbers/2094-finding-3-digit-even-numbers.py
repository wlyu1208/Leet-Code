class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        from collections import Counter

        freq = Counter(digits)
        res = []

        for n in range(100, 1000, 2):
            parts = [n // 100, (n // 10) % 10, (n % 10)]
            count = Counter(parts)

            if all(count[d] <= freq[d] for d in count):
                res.append(n)
        
        return res
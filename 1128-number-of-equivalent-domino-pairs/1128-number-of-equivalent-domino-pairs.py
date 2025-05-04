class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        counter = defaultdict(int)
        result = 0

        for a, b in dominoes:
            key = tuple(sorted((a, b)))
            counter[key] += 1
        
        for k, v in counter.items():
            if v > 1:
                result += (v * (v-1) // 2)
        return result


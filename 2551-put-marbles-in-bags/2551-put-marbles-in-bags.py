class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1: return 0

        possibles = []
        for i in range(len(weights)-1):
            possibles.append(weights[i] + weights[i+1])
        
        possibles.sort()


        return sum(possibles[-(k-1):]) - sum(possibles[:k-1])
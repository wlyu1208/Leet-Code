class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        real, temp_score = 0, 0
        i, j = 0, len(tokens) - 1

        while i <= j:
            if power >= tokens[i]:
                temp_score += 1
                power -= tokens[i]
                i += 1
                real = max(real, temp_score)
            elif temp_score > 0:
                power += tokens[j]
                temp_score -= 1
                j -= 1
            else:
                break
        
        return real


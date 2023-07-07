class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def count(letter):
            left = 0
            cnt = k
            result = 0

            for right in range(len(answerKey)):
                if answerKey[right] != letter:
                    cnt -= 1
                    while cnt < 0:
                        if answerKey[left] != letter:
                            cnt += 1
                        left += 1
                result = max(result, right - left + 1)
            return result

        return max(count('T'), count('F'))

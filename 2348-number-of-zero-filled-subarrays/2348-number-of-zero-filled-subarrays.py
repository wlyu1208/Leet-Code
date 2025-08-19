class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        answer = 0
        prev_cnt = 0

        for n in nums:
            if n == 0:
                prev_cnt += 1
                answer += prev_cnt
            else:
                prev_cnt = 0
            # print(n, prev_cnt, answer)

        return answer
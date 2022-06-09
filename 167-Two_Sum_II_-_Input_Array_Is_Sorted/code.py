class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        
        answer = []
        while i < j:
            cur_sum = numbers[i] + numbers[j]
            if cur_sum == target:
                answer.append(i + 1)
                answer.append(j + 1)
                return answer
            elif cur_sum < target:
                i += 1
            else:
                j -= 1

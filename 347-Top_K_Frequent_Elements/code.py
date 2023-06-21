class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        _dict = dict()

        for x in nums:
            if x not in _dict:
                _dict[x] = 1
            else:
                _dict[x] += 1

        answer = list()
        for key, val in sorted(_dict.items(), key = lambda x: x[1], reverse=True):
            answer.append(key)

            if len(answer) == k:
                break
        
        return answer

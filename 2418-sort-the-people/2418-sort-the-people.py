class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        _dict = {}

        for n, h in zip(names, heights):
            _dict[h] = n
        
        sorted_dict = dict(sorted(_dict.items(), key=lambda item: item[0], reverse=True))

        return sorted_dict.values()
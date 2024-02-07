class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        _map = defaultdict(list)

        for _str in strs:
            str_cnt = tuple(sorted(Counter(_str).items()))
            _map[str_cnt].append(_str)
        
        return list(_map.values())
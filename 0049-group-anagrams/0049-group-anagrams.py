class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        @cache
        def _sort(_str):
            return sorted(_str)

        groups = dict()

        for word in strs:
            key = "".join(_sort(word))

            if key not in groups:
                groups[key] = [word]
            else:
                groups[key].append(word)
        
        return groups.values()
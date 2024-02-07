class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = dict()

        for word in strs:
            key = "".join(sorted(word))

            if key not in groups:
                groups[key] = [word]
            else:
                groups[key].append(word)
        
        return groups.values()
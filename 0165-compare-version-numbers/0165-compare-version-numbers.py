class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        _max = max(len(v1), len(v2))

        ans = 0
        for i in range(_max):
            one = int(v1[i]) if i < len(v1) else 0
            two = int(v2[i]) if i < len(v2) else 0
            
            if ans == 0 and one < two:
                ans = -1
            if ans == 0 and one > two:
                ans = 1
        
        return ans
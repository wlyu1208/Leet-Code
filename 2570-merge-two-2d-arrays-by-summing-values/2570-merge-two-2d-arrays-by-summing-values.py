class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        _dict = defaultdict(int)

        for k, v in nums1:
            _dict[k] += v
        
        for k, v in nums2:
            _dict[k] += v
        ans = [(k, v) for k, v in _dict.items()]
        return sorted(ans, key=lambda x: x[0])
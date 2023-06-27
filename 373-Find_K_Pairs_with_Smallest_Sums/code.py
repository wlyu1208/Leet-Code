class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        h = list()

        for i in range(min(k, len(nums1))):
            heapq.heappush(h, (nums1[i] + nums2[0], nums1[i], nums2[0], 0))
        
        result = list()

        while h and len(result) < k:
            _sum, n1, n2, idx2 = heapq.heappop(h)

            result.append([n1, n2])
            
            if idx2+1 < len(nums2):
                idx2 += 1
                heapq.heappush(h, (n1+nums2[idx2], n1, nums2[idx2], idx2))

        return result

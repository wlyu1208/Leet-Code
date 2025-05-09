class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0: return
        total = len(nums1)
        back_idx = total - 1
        while n > 0 and m > 0:
            if nums2[n-1] >= nums1[m-1]:
                nums1[back_idx] = nums2[n-1]
                n-=1
            else:
                nums1[back_idx] = nums1[m-1]
                m-=1
            back_idx-=1
        while n > 0:
            nums1[back_idx] = nums2[n-1]
            n-=1
            back_idx -=1
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return list()
            
        n = len(nums)

        start = nums[0]
        end = nums[0]

        result = list()

        for i in range(1, n):
            if nums[i] == end + 1:
                end = nums[i]
            else:
                if start == end:
                    result.append(f"{end}")
                else:
                    result.append(f"{start}->{end}")
                start = nums[i]
                end = nums[i]
        
        if start == end:
            result.append(f"{end}")
        else:
            result.append(f"{start}->{end}")

        return result

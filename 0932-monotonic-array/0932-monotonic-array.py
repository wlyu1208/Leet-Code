class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
      is_inc, is_dec = False, False

      for i in range(1, len(nums)):
        if nums[i] - nums[i - 1] == 0: 
          continue
        elif nums[i] - nums[i - 1] > 0: 
          is_inc = True
        elif nums[i] - nums[i-1] < 0: 
          is_dec = True
      
      return False if is_inc and is_dec else True
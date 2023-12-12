class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> numMap = new HashMap<>();

        for (int i=0; i<nums.length; i++) {
            numMap.put(nums[i], i);
        }

        for (int i=0; i<nums.length; i++) {
            int rest = target - nums[i];
            if (numMap.containsKey(rest) && numMap.get(rest) != i) {
                return new int[] {i, numMap.get(rest)};
            }
        }
        return new int[] {};
    }
}
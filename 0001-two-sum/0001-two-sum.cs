public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        Dictionary<int, int> numMap = new Dictionary<int, int>();

        for (int i=0; i< nums.Length; i++){
            int rest = target - nums[i];
            if (numMap.ContainsKey(rest)){
                return new int[] {numMap[rest], i};
            }
            numMap[nums[i]] = i;
        }
        return new int[] {};
    }
}
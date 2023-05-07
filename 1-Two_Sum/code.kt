class Solution {
    fun twoSum(nums: IntArray, target: Int): IntArray {
        val ans = IntArray(2)
        val len_n = nums.size

        for (i in nums.indices) {
            val n = nums[i];
            for (j in i+1 until len_n) {
                val n2 = nums[j];
                if ((n + n2) == target) {
                    ans[0] = i;
                    ans[1] = j;
                }
            }
        }
        return ans
    }
}

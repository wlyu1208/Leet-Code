class Solution {
    fun twoSum(nums: IntArray, target: Int): IntArray {
        val hashmap = mutableMapOf<Int, Int>();

        for ( (i, v) in nums.withIndex() ) {
            val diff = target - v;
            val diff_idx = hashmap.get(diff);

            diff_idx?.let {
                return@twoSum intArrayOf(diff_idx, i)
            }

            hashmap[v] = i;
        }

        return intArrayOf()
    }
}


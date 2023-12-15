class Solution {
    public int majorityElement(int[] nums) {
        int cnt = 0;
        int ans = -1;

        for (int num: nums) {
            if (num == ans) {
                cnt++;
            }
            else if (cnt == 0) {
                ans = num;
                cnt = 1;
            }
            else {
                cnt--;
            }
        }
        return ans;
    }
}
class Solution {
    public void moveZeroes(int[] nums) {
        if (nums.length == 1) {
            return;
        }

        int cnt = 0;
        int[] answer = new int[nums.length];

        for (int i=0; i<nums.length; i++) {
            if (nums[i] != 0){
                nums[cnt] = nums[i];
                cnt++;
            }
        }
        while (cnt < nums.length) {
            nums[cnt] = 0;
            cnt++;
        }
    }
}
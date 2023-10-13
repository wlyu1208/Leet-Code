class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        List<Integer> ans = new ArrayList<>();
        int n = nums.length;
        int[] cnt = new int[n];
        for (int i=0; i<n; i++) cnt[nums[i]-1]++;
        for (int i=0; i<n; i++) if(cnt[i] == 0) ans.add(i + 1);
        return ans;
    }
}
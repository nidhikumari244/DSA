class Solution {

    long ans = Long.MIN_VALUE;

    public long maxStrength(int[] nums) {
        backtrack(nums, 0, 1L, false);
        return ans;
    }

    private void backtrack(int[] nums, int index, long product, boolean taken) {

        // Base case
        if (index == nums.length) {
            if (taken) {
                ans = Math.max(ans, product);
            }
            return;
        }

        // Include current element
        backtrack(nums, index + 1, product * nums[index], true);

        // Exclude current element
        backtrack(nums, index + 1, product, taken);
    }
}

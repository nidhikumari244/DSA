class Solution {

    int sum = 0;

    public int subsetXORSum(int[] nums) {
        backtrack(nums, 0, 0);
        return sum;
    }

    private void backtrack(int[] nums, int index, int xor) {

        // Base case
        if (index == nums.length) {
            sum += xor;
            return;
        }

        // Include current element
        backtrack(nums, index + 1, xor ^ nums[index]);

        // Exclude current element
        backtrack(nums, index + 1, xor);
    }
}

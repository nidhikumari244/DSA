class Solution {
    public int maximumStrongPairXor(int[] nums) {
        int maxXor = 0;

        for (int i = 0; i < nums.length; i++) {
            for (int j = i; j < nums.length; j++) {

                int x = nums[i];
                int y = nums[j];

                if (Math.abs(x - y) <= Math.min(x, y)) {
                    maxXor = Math.max(maxXor, x ^ y);
                }
            }
        }

        return maxXor;
    }
}

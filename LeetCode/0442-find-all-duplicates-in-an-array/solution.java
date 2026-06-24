class Solution {
    public List<Integer> findDuplicates(int[] nums) {
        List<Integer> result = new ArrayList<>();
        
        for (int num : nums) {
            int idx = Math.abs(num) - 1;       // map value to index
            if (nums[idx] < 0) result.add(idx + 1); // seen before → duplicate
            else nums[idx] = -nums[idx];            // mark as visited
        }
        
        return result;
    }
}

class Solution {
    public int[] limitOccurrences(int[] nums, int k) {
        List<Integer> result = new ArrayList<>();
        int count = 1;
        
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] == nums[i-1]) {
                count++;
            } else {
                count = 1;
            }
            if (count <= k) {
                result.add(nums[i]);
            }
        }
        
        // Add first element (always valid since k >= 1)
        result.add(0, nums[0]);
        
        return result.stream().mapToInt(Integer::intValue).toArray();
    }
}

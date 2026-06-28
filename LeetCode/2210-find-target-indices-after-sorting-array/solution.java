class Solution {
    public List<Integer> targetIndices(int[] nums, int target) {
        List<Integer> result = new ArrayList<>();
        
        int lessCount = 0;
        int equalCount = 0;
        
        for (int num : nums) {
            if (num < target)  lessCount++;
            if (num == target) equalCount++;
        }
        
        // target occupies indices: lessCount to lessCount + equalCount - 1
        for (int i = lessCount; i < lessCount + equalCount; i++) {
            result.add(i);
        }
        
        return result;
    }
}

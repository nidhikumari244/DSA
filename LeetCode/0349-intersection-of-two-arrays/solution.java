class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        Set<Integer> set1 = new HashSet<>();
        Set<Integer> result = new HashSet<>();
        
        for (int n : nums1) set1.add(n);
        for (int n : nums2) {
            if (set1.contains(n)) result.add(n);
        }
        
        return result.stream().mapToInt(Integer::intValue).toArray();
    }
}

class Solution {
    public int thirdMax(int[] nums) {
        Set<Long> seen = new HashSet<>();
        Long first = null, second = null, third = null;
        
        for (int num : nums) {
            long n = (long) num;
            if (!seen.add(n)) continue;
            
            if (first == null || n > first) {
                third = second;
                second = first;
                first = n;
            } else if (second == null || n > second) {
                third = second;
                second = n;
            } else if (third == null || n > third) {
                third = n;
            }
        }
        
        // Fix: cast each Long separately before the ternary
        return third != null ? third.intValue() : first.intValue();
    }
}

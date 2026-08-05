class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {

        HashMap<Integer, Integer> map = new HashMap<>();

        // Store frequencies of nums1
        for (int num : nums1) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }

        List<Integer> result = new ArrayList<>();

        // Find common elements
        for (int num : nums2) {
            if (map.getOrDefault(num, 0) > 0) {
                result.add(num);
                map.put(num, map.get(num) - 1);
            }
        }

        // Convert List to Array
        int[] ans = new int[result.size()];
        for (int i = 0; i < result.size(); i++) {
            ans[i] = result.get(i);
        }

        return ans;
    }
}

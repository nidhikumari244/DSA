class Solution {

    public List<List<Integer>> subsets(int[] nums) {

        List<List<Integer>> ans = new ArrayList<>();
        List<Integer> current = new ArrayList<>();

        backtrack(0, nums, current, ans);

        return ans;
    }

    private void backtrack(int index, int[] nums,
                           List<Integer> current,
                           List<List<Integer>> ans) {

        if (index == nums.length) {
            ans.add(new ArrayList<>(current));
            return;
        }

        // Take
        current.add(nums[index]);
        backtrack(index + 1, nums, current, ans);

        // Undo (Backtrack)
        current.remove(current.size() - 1);

        // Don't Take
        backtrack(index + 1, nums, current, ans);
    }
}

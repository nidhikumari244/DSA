class Solution {
    public TreeNode sortedArrayToBST(int[] nums) {
        return build(nums, 0, nums.length - 1);
    }
    
    private TreeNode build(int[] nums, int left, int right) {
        if (left > right) return null;          // Base case
        
        int mid = left + (right - left) / 2;   // Avoid overflow
        
        TreeNode root = new TreeNode(nums[mid]);
        root.left  = build(nums, left, mid - 1);   // Left half
        root.right = build(nums, mid + 1, right);  // Right half
        
        return root;
    }
}

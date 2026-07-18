/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {

    // Helper function for recursive postorder traversal.
    // Order:
    // 1. Left subtree
    // 2. Right subtree
    // 3. Current node
    public void postorder(TreeNode root, List<Integer> ans) {

        // Base case
        if (root == null) {
            return;
        }

        // Traverse left subtree.
        postorder(root.left, ans);

        // Traverse right subtree.
        postorder(root.right, ans);

        // Visit current node.
        ans.add(root.val);
    }

    public List<Integer> postorderTraversal(TreeNode root) {

        // Stores traversal result.
        List<Integer> ans = new ArrayList<>();

        // Start recursion.
        postorder(root, ans);

        return ans;
    }
}

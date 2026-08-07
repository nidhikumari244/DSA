class Solution {
    public boolean isCousins(TreeNode root, int x, int y) {
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);

        while (!queue.isEmpty()) {
            int size = queue.size();
            TreeNode parentX = null, parentY = null;

            for (int i = 0; i < size; i++) {
                TreeNode node = queue.poll();

                if (node.left != null) {
                    if (node.left.val == x) parentX = node;
                    if (node.left.val == y) parentY = node;
                    queue.offer(node.left);
                }
                if (node.right != null) {
                    if (node.right.val == x) parentX = node;
                    if (node.right.val == y) parentY = node;
                    queue.offer(node.right);
                }
            }

            // Both found at this level
            if (parentX != null && parentY != null) {
                return parentX != parentY;
            }
            // Only one found at this level -> different depths, can't be cousins
            if (parentX != null || parentY != null) {
                return false;
            }
        }

        return false;
    }
}

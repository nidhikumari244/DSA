class BSTIterator {
    private Stack<TreeNode> stack = new Stack<>();
    
    public BSTIterator(TreeNode root) {
        pushLeft(root);  // Initialize with leftmost path
    }
    
    public int next() {
        TreeNode node = stack.pop();       // Smallest remaining
        pushLeft(node.right);              // Explore right subtree
        return node.val;
    }
    
    public boolean hasNext() {
        return !stack.isEmpty();
    }
    
    // Push all left children of a node onto the stack
    private void pushLeft(TreeNode node) {
        while (node != null) {
            stack.push(node);
            node = node.left;
        }
    }
}

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """

        def isSameTree(a, b):
            if not a and not b:
                return True
            if not a or not b:
                return False
            return (a.val == b.val 
                    and isSameTree(a.left, b.left) 
                    and isSameTree(a.right, b.right))
        
        def dfs(node):
            if not node:
                return False
            if isSameTree(node, subRoot):
                return True
            return dfs(node.left) or dfs(node.right)
        
        return dfs(root)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMode(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """

        
        self.count = 0
        self.max_count = 0
        self.prev = None
        self.modes = []
        
        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            
            # Process current node
            if self.prev is not None and self.prev.val == node.val:
                self.count += 1
            else:
                self.count = 1
            
            if self.count > self.max_count:
                self.max_count = self.count
                self.modes = [node.val]
            elif self.count == self.max_count:
                self.modes.append(node.val)
            
            self.prev = node
            
            inorder(node.right)
        
        inorder(root)
        return self.modes

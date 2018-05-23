class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root== None:
            return 0
        return 1 + max(maxDepth(root.left), maxDepth(root.right))
        
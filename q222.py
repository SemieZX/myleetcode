class Solution:
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        int height(root):
            if root == None:
                return -1
            else:
                return 1 + height(root.left)
        h = height(root)
        if h < 0:
            return 0
        elif height(root.right) == h-1:
            return (1<<h) + self.countNodes(root.right)
        else:
            return (1<<h-1) + self.countNodes(root.left)

class Solution:
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        return 1 + self.countNodes(root.left) +self.countNodes(root.right)
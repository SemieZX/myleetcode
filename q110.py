class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def height(root):
            if root == None:
                return 0
            return max(height(root.left),height(root.right)) + 1

        if root == None:
            return True
        return abs(height(root.left),height(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)


class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def dfsheight(root):
            if root == None:
                return 0
            lh = dfsheight(root.left)
            if (lh == -1):
                return -1
            rh = dfsheight(root.right)
            if (rh == -1):
                return -1
            if abs(lh-rh) > 1:
                return -1
            return max(lh,rh) + 1
        return dfsheight(root) != -1

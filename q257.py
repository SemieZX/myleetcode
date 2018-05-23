class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res = []
        if root == None:
            return res
        if root.left == None and root.right == None:
            res.append(str(root.val))
            return res
        
        leftpath = self.binaryTreePaths(root.left)
        for item in leftpath:
            sb = str(root.val)
            sb += "->"
            sb += item
            res.append(sb)
        
        rightpath = self.binaryTreePaths(root.right)
        for item in rightpath:
            sb = str(root.val)
            sb += "->"
            sb += item
            res.append(sb)
        return res
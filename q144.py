class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = [ ]
        if root:
            res.append(root.val)
            res += self.preorderTraversal(root.left)
            res += self.preorderTraversal(root.right)
        return res

    def preorderTraversal1(self,root):
        res = [ ]
        stack = [ ]
        while root :
            res.append(root.val)
            if root.right:
                stack.append(root.right)
            root = root.left
            if root==None and stack:
                root = stack.pop()
        return res

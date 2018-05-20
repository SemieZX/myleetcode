class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = [ ]
        if root:
            res += self.inorderTraversal(root.left)
            res.append(root.val)
            res += self.inorderTraversal(root.right)
        return res
    def  inorderTraversal2(self,root):

        res = [ ]
        stack = [ ]
        cur = root
        while  cur  or stack:
            while cur :
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            # maybe there is a one right node
            cur = cur.right
        return res
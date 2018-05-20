class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = [ ]
        if root:
            res += self.postorderTraversal(root.left)
            res += self.postorderTraversal(root.right)
            res.append(root)
        return res

    def postorderTraversal1(self,root):
        res = [ ]
        stack = [ ]
        p = root
        while stack and p :
            if p :
                stack.append(p)
                result.inset(0,p.val)
                p = p.right
            else:
               node = stack.pop()
               p = node.left
        return result
        
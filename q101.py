class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
        	return True
        return self.Mirrors(root.left,root.right)
    def Mirrors(self, left, right):

    	if left == None or right == None:
    		return  left == right
    	return left.val == right.val && self.Mirrors(left.left,right.right)&& self.Mirrors(left.right,right.left)
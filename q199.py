class Solution:
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # each level of the tree only select one node
        #  view level is current size of result list
        res = [ ]
        self.rightview(root,res,0)
        return res
    def rightview(cur, res, curlevel):
        if cur == None:
            return 
        if curlevel == len(res):
            res.append(cur.val)
        rightview(cur.right,res,curlevel+1)
        rightview(cur.left,res,curlevel+1)

        
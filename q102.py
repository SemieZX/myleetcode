from collections import deque
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = [ ]
        if root ==None:
            return res

        queue = deque([[root,0]])
        while queue:
            front =queue.popleft()
            node = front[0]
            level = front[1]

            if level == len(res):
                res.append([  ])
            assert level < len(res)

            res[level].append(node.val)

            if node.left :
                queue.append([[node.left, level+1]])
            if node.right:
                queue.append([[node.right, level+1]])
        return res
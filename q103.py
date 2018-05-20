class Solution:
    def zigzagLevelOrder(self,root):
        queue, res = collections.deque([(root,0)]), [ ]
        while queue:
            node,level = queue.popleft()
            if node:
                if len(res) < level+1:
                    res.append([ ])
                res[level].append(node.val)
                queue.append((node.left, level+1))
                queue.append((node.right, level+1))
        for i in range(1,len(res),2):
            res[i] = res[i][: : -1]

        return res


class Solution:
    def zigzagLevelOrder(self,root):
        res = [ ]
        self.travel(root,res,0)
        return res
    def travel(self,root,res,level):
        if root == None:
            return 
        if len(res) < level+1:
            res.append([  ])

        if level%2 == 0:
            res[level].append(root.val)
        else:
            res[level].insert(0,root.val)

        self.travel(root.left,res,level+1)
        self.travel(root.right,res,level+1)
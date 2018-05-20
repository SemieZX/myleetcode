## Time limited exceeded
class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0 :
            return 0
        presqure = [ 10000 for i in range(n+1 )  ]
        presqure[0] = 0
        for i in range(1,n+1):
            j = 1
            #for each i ,it must be the sum of some number i-j**2 and a perfect
            # square number j**2 
            while j**2  <= i:
                presqure[i] = min(presqure[i], presqure[i-j**2]+1)
                j += 1
        return presqure[-1]

class Solution:
    def numSquares(target):
        level ,targets = 0, set({target})
        roots = set([(x+1)**2 for  x in range(int(target**0.5)) ])

        while targets:
            # if targets and roots have the same item , then make targets None
            targets  = None if targets.intersection(roots) else set([x-y for x in targets for y in roots if x-y >0])
            level += 1
        return level

from collections import deque
class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 0

        queue = deque([(n,0)])
        visited = [ False for i in range(n+1) ]
        visited[n] = True

        while queue:
            front = queue.popleft()
            num = front[0]
            step = front[1]

            if num == 0:
                return step

            i = 1
            while num - i*i >= 0:
                a = num -i*i
                if visted[a]==False:
                    if a==0 : return step+1
                    queue.append((num -i*i), step+1)
                    visited[num -i*i] = True
                i +=  1

class Solution:
    def numSquares(self,n):
        if n==0: return 0
        queue = collections.deque([(n,0)])

        visited = [False for i in range(n+1)]
        visited[n] = True
 
        while queue:
            front= queue.popleft()
            num =front[0]
            step = front[1]

            i = 1
            while num - i**2 >= 0:
                a = num - i*i
                if visited[a] == False:
                    if a==0 : return step + 1
                    queue.append((a,step+1))
                    visited[a] = True
                i += 1
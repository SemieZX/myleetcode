class Solution:
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        def distance(pa , pb):
            return (pa[0] - pb[0])**2 + (pa[1]-pb[1])**2
        res = 0
        for i in range(len(points)):
            d=  { }
            for j in range(len(points)):
                if j != i:
                    dis = distance(points[i],points[j])
                    if dis in d:
                        d[dis] += 1
                    else:
                        d[dis] = 1
            for dis in d.keys():
                res += d[dis]*(d[dis]-1)
        return res
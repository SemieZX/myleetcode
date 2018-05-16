# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if len(points)  == 1:
            return 1
        if len(points)  == 0:
            return 0
        def calline(point1,point2 ):
            if point2.x != point1.x:
                a = (point2.y -point1.y)/(point2.x-point1.x)
                #b = point2.y - a*point2.x
            else:
                a = 0
                #b =  1
            return a
        
        res = 0
        for i in range(len(points)):
            d = { }
            same_number = 1
            for j in range(len(points)):
                if i !=j:
                    if points[i].x == points[j].x and points[i].y ==points[j].y:
                        same_number += 1
                    else:
                        tu = calline(points[i],points[j])
                        if tu in d:
                            d[tu] += 1
                        else:
                            d[tu] = 1
            if d =={}:
                res_temp = same_number
            else:
                res_temp = max(value for value in d.values()) + same_number
            res = max( res , res_temp)
        return res
class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l , r = 0, len(height) - 1
        low = min(height[l],height[r])
        most = (r-l)*low
        while l < r:
            if low == height[l] and l < r:
                l += 1
                low = min(height[l],height[r])
                most  = max(most,(r-l)*low)
            elif low == height[r] and l < r:
                r -= 1
                low = min(height[l],height[r])
                most  = max(most,(r-l)*low)
        return most

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l , r = 0 ,len(height)-1
        most = 0
        while l < r:
            h = min(height[l],height[r])
            most = max(h *(r-l),most)
            if l< r and h ==height[l]:
                l +=1
            elif l < r and h ==height[r]:
                r -= 1
        return most
                
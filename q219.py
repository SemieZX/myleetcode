class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) <= 1:
            return False
        if k < 0:
            return False
        d = { }
        for i ,v in enumerate(nums):
            if v in d:
                return True
            d[v] = 1
            if len(d)==k+1: #think about what will happen?
                d.pop(nums[i-k])
        return False
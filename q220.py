class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if len(nums) < 2 or t < 0:
            return False
        w = t + 1
        d = {}
        for i in range(len(nums)):
            m = nums[i] // w
            if m in d:
                return True
            elif (m - 1 in d) and abs(nums[i] - d[m - 1]) < w:
                return True
            elif (m + 1 in d) and abs(nums[i] - d[m + 1]) < w:
                return True
            else:
                d[m] = nums[i]
                if i >= k:
                    del d[nums[i - k] // w]
return False
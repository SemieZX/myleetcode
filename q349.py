class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1_set = set(nums1)
        nums2_set = set(nums2)
        res =[]
        for item in nums1_set:
            if item in nums2_set:
                res.append(item)
        return res
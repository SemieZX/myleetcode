class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1_dict = collections.Counter(nums1)
        #for item in nums1:
            #nums1_dict[item] += 1
        nums2_dict = collections.Counter(nums2)
        #for item in nums2:
            #1nums2_dict[item] += 1
        res = []
        for item in nums1_dict:
            if item in nums2_dict:
                small = min(nums1_dict[item],nums2_dict[item])
                for i in range(small):
                    res.append(item)
        return res
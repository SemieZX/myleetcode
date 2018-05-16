class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        counter_dict = collections.Counter(nums)
        for value in counter_dict.values():
            if value >= 2:
                return True
        return False
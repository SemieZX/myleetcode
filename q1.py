class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sol_dict = {}
        for index , item in enumerate(nums):
            if target - item in sol_dict:
                return [index,sol_dict[target-item]]
            sol_dict [item] = index
            
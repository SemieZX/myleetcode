class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        def swaps(nums,i,j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
        
        k = 0 
        for i, item in enumerate(nums):
            if item != val:
                nums[k] = item
                k += 1
        return k

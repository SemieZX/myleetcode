class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        for item in nums:
            
            if i<2 or item > nums[i-2]:
                nums[i] = item
                i += 1
        return i 
       

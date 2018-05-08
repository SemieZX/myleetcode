# two flag ,newtails is smaller than i
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        newtails = 0
        for i in range(1,len(nums)):
            if nums[newtails] != nums[i]:
                newtails += 1
                nums[newtails] = nums[i]
        return newtails + 1
        

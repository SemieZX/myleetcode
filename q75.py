class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        lenth = len(nums)
        origin = -1
        def switch(nums,t,k):
            temp = nums[t]
            nums[t] = nums[k]
            nums[k] = temp
        i = 0
        while i < lenth:
            if nums[i] == 1:
                i += 1
            elif nums[i] == 2:
                lenth -= 1
                switch(nums,i,lenth)
            else:
                assert nums[i] == 0
                origin += 1
                switch(nums,i,origin)
                i += 1

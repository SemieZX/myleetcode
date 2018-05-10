class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def swap(nums,i,j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
        def partition(nums,l,r):
            tar = nums[l]
            j = l
            i = l+1
            while i <= r:
                if nums[i] < tar:
                    j += 1
                    swap(nums,j,i)
                i += 1
            swap(nums,l,j)
            return j
        
        lenth =len(nums)
        l = 0
        r = len(nums) -1
        while True:
            pos = partition(nums,l,r)
            if pos > lenth - k:
                l = 0
                r = pos - 1
            elif pos < lenth - k:
                l = pos + 1
                r = r
            else:
                return nums[pos]

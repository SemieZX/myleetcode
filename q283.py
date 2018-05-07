class Solution:

    def moveZeroes(self, nums):

        def swaps(nums, t, j):
            temp = nums[t]
            nums[t] = nums[j]
            nums[j] = temp
        
        k = 0
        for i, item in enumerate(nums):
            if item != 0:
                swaps(nums,k,i)
                k += 1
        return nums
L = [1,0,4,0,5,0,12]
test = Solution()
print(test.moveZeroes(L))

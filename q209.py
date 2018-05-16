class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        lenth = len(nums)
        mysum = [0 for i in range(lenth+1)]
        res = lenth +1
        for i in range(1,lenth+1):
            mysum[i] = mysum[i-1] + nums[i-1]
        for i in range(lenth):
            for j in range(i,lenth):
                if(mysum[j+1] - mysum[i] >= s):
                    res = min(res, j-i+1)
        if(res == lenth + 1):
            return 0
        return res
class Solution:
    def lengthOfLongestSubstring(self,s):

        start  = 0
        prefix = {}
        res = 0
        for index,character in enumerate(s):
            if character in prefix and prefix[character] >= start:
                start = prefix[character] + 1
            prefix[character] = index
            res = max(res,index-start+1)
        return res

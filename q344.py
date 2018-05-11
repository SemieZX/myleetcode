class Solution:
    def reverseString(self,s):
        res = ""
        lenth = len(s)
        for i in range(lenth):
            res += s[lenth-1-i]
        return res

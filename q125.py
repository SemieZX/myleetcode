import re
class Solution:
    def isPalindrome(self,s):

        s = s.lower()
        s = re.sub('[^a-zA-Z0-9]','',s)
        return s == s[::-1]

    def isPalindrome2(self,s):
        l ,r = 0 ,len(s) -1
        while l < r:
            while l < r  and not s[l].isalnum():
                l += 1
            while l < r  and not s[l].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True





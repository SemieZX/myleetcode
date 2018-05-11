def reverseVowels(self,s):
    if s == "":
        return s
    l ,r = 0, len(s)-1
    res = [o for i in range(r+1))]
    while l < r:
        while l<r and s[l]not in ['a','e','i','o','u','A','E','I','O','U']:
            res[l] = s[l]
            l += 1
        while l<r and s[r]not in ['a','e','i','o','u','A','E','I','O','U']:
            res [r] = s[r]
            r -= 1
        res[r] = s[l]
        res[l] = s[r]
        l += 1
        r -= 1
    return "".join(res)
    

def reverseVowels(self, s):
    """
    :type s: str
    :rtype: str
    """
    if s == "":
        return s
    l ,r = 0, len(s) - 1
    mylist = list(s)
    mydir = "aeiouAEIOU"
    while l < r:
        while mylist[l] not in mydir  and l < r:
            l += 1
        while mylist[r] not in mydir and l < r:
            r -= 1
        mylist[l] , mylist[r] = mylist[r] , mylist[l]
        l += 1
        r -= 1
    return "".join(mylist)
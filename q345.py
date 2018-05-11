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

class Solution(object):
    def findAnagrams(self,s,p):
        if len(s)<len(p) or not s or not p:
            return []

        need = collections.Counter(p)
        res = []
        l, r, missing = 0, 0, len(p)

        while r < len(s):
            if need[s[r]] > 0:
                missing -= 1
            need[s[r]] -= 1

            if missing == 0:
                res.append(1)

            if r-l == len(p) - 1:
                needs[s[l]] += 1
                if needs[s[l]] > 0:
                    missing += 1
                l += 1
            r += 1
        return res[]

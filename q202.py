class Solution:
    def isHappy(self,n):
        return self.check(n,set())
    def check(self,n,hashSet):
        if n in hashSet:
            return Fasle
        else:
            happysum = sum([int(i)**2 for i in list(str(n))])
            if happysum == 1:
                return True
            else:
                hashSet.add(n)
                return self.check(happysum,hashSet)
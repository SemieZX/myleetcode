class Soulution:
    def twoSum(self,numbers,target):

        l = 0
        r = len(numbers)-1

        while l < r:
            if numbers[l] + numbers[r] == target:
                res = (l+1,r+1)
                return res
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else:
                l += 1

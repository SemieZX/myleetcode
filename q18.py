class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
        num.sort()
        def ksum(num, k, target):
            i = 0
            result = set()
            if k == 2:
                j = len(num) - 1
                while i < j:
                    if num[i] + num[j] == target:
                        result.add((num[i], num[j]))
                        i += 1
                    elif num[i] + num[j] > target:
                        j -= 1
                    else:
                        i += 1
            else:
                while i < len(num) - k + 1:
                    newtarget = target - num[i]
                    subresult = ksum(num[i+1:], k - 1, newtarget)
                    if subresult:
                        result = result | set( (num[i],) + nr for nr in subresult)
                    i += 1
                
            return result
        
        return [list(t) for t in ksum(num, 4, target)]
        
        
    def foursum(self,nums,target):
        def findNsum(nums,target,N,result,results):
            if len(nums) < N or N < 2 or target < nums[0] * N or nums[-1]*N:
                return
            if N == 2:
                l,r = 0, len(nums)-1
                while l<r:
                    s = sums[l] +nums[r]
                    if s==target:
                        results.append(result+[num[l],num[r]])
                        l += 1
                    elif s < target:
                        l +=1
                    else:
                        r -=1
            else:
                for i in range(len(nums)-N+1):
                    if i ==0 or (i>0 and nums[i-1] != nums[i]):
                        findNsum(nums[i+1:],target-nums[i],N-1,result +[nums[i],results])
    results = []
    findNsum(sorted(nums),target,4,[],results)
    return results
                    
import heapq
class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        d = collections.Counter(nums)
        list_d = [[va,key] for key,va in d.items()]
        n = len(list_d)
        heapq.heapify(list_d)
        for i in range(n-k):
            heapq.heappop(list_d)
        for i in range(k):
            res.append(heapq.heappop(list_d)[1])
        return res
        
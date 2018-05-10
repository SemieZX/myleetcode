import heapq
classs Solution:
    def findKthLargest(self,nums,k):

        heapq.heapify(nums)

        for i in range(len(nums)-k):
            heapq.heappop(nums)
        value_k = heapq.heappop(nums)
        return value_k


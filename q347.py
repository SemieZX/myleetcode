class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        num_count = collections.Counter(nums)
        return heapq.nlargest(k,num_count,key = lambda x: num_count[x])
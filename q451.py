class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_dict = collections.Counter(s)

        res = []
        sorted_dict = sorted(s_dict.items(),key = lambda x :x[1],reverse =True)
        
        lenth = len(sorted_dict)
        for i in range(lenth):
            j = 0
            while j < sorted_dict[i][1]:
                res.append(sorted_dict[i][0])
                j += 1 
        
        return ''.join(res)
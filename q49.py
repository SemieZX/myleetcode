class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        dict_s = { }
        for s in strs:
            if str(sorted(s))  in dict_s:
                dict_s[str(sorted(s))].append(s)
            else:
                dict_s[str(sorted(s))] = [s]
        res = [ value for value in dict_s.values()]
        return res

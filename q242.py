class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_dict = collections.Counter(s)
        t_dict = collections.Counter(t)
        
        if len(s) != len(t):
            return False
        
        for item in s_dict:
            if s_dict[item] != t_dict[item]:
                return False
        return True
                
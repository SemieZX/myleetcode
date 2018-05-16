class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == "":
            return True
        s_dict = {}
        for index,item in enumerate(s):
            if item not in s_dict:
                s_dict[item] = []
            s_dict[item].append(index)
        t_dict = {}
        for index, item in enumerate(t):
            if item not in t_dict:
                t_dict[item] = []
            t_dict[item].append(index)
        
        t_dict_value = t_dict.values()
        for key_s in s_dict:
            if s_dict[key_s]  not in t_dict_value:
                return False
        return True
        
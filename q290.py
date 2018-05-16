class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str_list = list(str.split(' '))
        str_dict = {}
        hash1Set = set(str_list)
        hash2Set = set(pattern)
        if len(hash1Set) != len(hash2Set):
            return False
        if len(str_list) != len(pattern):
            return False
        
        for index, item in enumerate(pattern):
            if item not in str_dict:
                str_dict[item] = []
            str_dict[item].append(index)
           
        for key in str_dict:
            for index in str_dict[key]:
                if str_list[str_dict[key][0]] != str_list[index]:
                    return False
        return True
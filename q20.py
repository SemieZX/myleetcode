class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lenth = len(s)
        stack = [ ]
        for i in range(lenth):
            if s[i] == '(':
                stack.append(')')
            elif s[i] == '{':
                stack.append('}')
            elif s[i] == '[':
                stack.append(']')
            else:
                if len(stack) == 0 or stack.pop()!= s[i]:
                    return False
        return len(stack) == 0

     def isValid2(self,s):
        lenth = len(s)
        stack = []
        for i in range(lenth):
            if s[i]  in ('(' , '[' ,'{'):
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                c = stack.pop()
                match = ' '

                if (s[i] == ')'):
                    match = '('
                elif(s[i]==']'):
                    match = '['
                else:
                    match= '{'
                if match != c:
                    return False
        if len(stack) != 0:
            return False
        return True



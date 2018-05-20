class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = [ ]
        for to in tokens:
            if to not in "+-*/":
                stack.append(int(to))
            else:
                num2 = stack.pop()
                num1 = stack.pop()

                if to== '+':
                    stack.append(num1+num2)
                elif to == '-':
                    stack.append(num1 - num2)
                elif to== '*':
                    stack.append(num1*num2)
                elif to== '/':
                    stack.append(int(num1/num2))
        res = stack.pop()
        return res

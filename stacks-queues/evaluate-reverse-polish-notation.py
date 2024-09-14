class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for i in tokens:
            if self.is_integer(i):
                stack.append(int(i)) ## 10
                result = stack[0]
            else:
                b = stack.pop() 
                a = stack.pop() 
                result = self.operation(i, a, b) 
                stack.append(result)
                print(i, a, b, result)            
        return result

    def is_integer(self, number):
        try:
            int(number)
            return True
        except:
            return False
                
    def operation(self, operation, a, b):
        if (operation == '+'):
            return a + b
        elif (operation == '-'):
            return a - b
        elif (operation == '*'):
            return a * b
        else: 
            if (a * b < 0 and a % b != 0 ):
                return a//b + 1
            else:
                return a//b

## complexidade de espaco O(n)
## complexidade de tempo O(n)

## https://leetcode.com/problems/evaluate-reverse-polish-notation/
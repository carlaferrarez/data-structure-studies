class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool

            ## for each char that is type open, i`ll add in my stack
            ## if I find a char that is close and my stack is empty then I could return False
            ## when I find the first one that is not open, then I`ll start comparing the chars
            ## if the first close one is equal to the top of the stack than
            ## they are complementaries, I`ll pop the stack and continue doing that
            ## if not, i`ll return false
            ## by the end, if I finish my s_list and the stack is empty, i could return true
            ## 
            ##  s = "(]"
            ## s_list = ["(", "]"]
        """
        s_list= list(s)
        stack = []

        for s_character in s_list:

            if (s_character == "(" or s_character == "{" or s_character == "["):
                stack.append(s_character)
            if (stack == [] and (s_character == ")" or s_character == "}" or s_character == "]")):
                return False
            
            if (s_character == ")" or  s_character == "}" or s_character == "]"):
                top_stack = stack.pop()
                if (s_character == ")" and (top_stack == "{" or top_stack == "[")):
                    return False
                if (s_character == "}" and (top_stack == "(" or top_stack == "[")):
                    return False
                if (s_character == "]" and (top_stack == "(" or top_stack == "{")):
                    return False
        if stack == []:
            return True
        return False
        
## time complexity = O(n)
## space complexity = O(n)

## https://leetcode.com/problems/valid-parentheses/description/
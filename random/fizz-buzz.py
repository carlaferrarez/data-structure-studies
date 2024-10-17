class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        answer = list()
        for i in range(1, n+1):
            if (i == 1 or i == 2):
                answer.append(str(i)) 
            elif (i%3 == 0):
                if (i%5 == 0):
                    answer.append("FizzBuzz")
                else:
                    answer.append("Fizz")
            elif (i%5 == 0):
                answer.append("Buzz")
            else:
                answer.append(str(i))
        return answer

# https://leetcode.com/problems/fizz-buzz/


        
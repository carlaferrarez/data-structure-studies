class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        if (k > len(arr)):
            return ""
        stack=[]
        size = len(arr) 
        
        while(size != 0):
            value = arr[size - 1]
            count_number = arr.count(value)
            if (count_number > 1):
                for i in range(count_number):
                    arr.remove(value)
            else:
                stack.append(value)
                arr.pop()
            size = len(arr)

        if (k <= len(stack)):
            return stack[len(stack) - k]
        else:
            return ""                    

# complexidade de espaço: O(n)
# complexidade de tempo: O(n)
# https://leetcode.com/problems/kth-distinct-string-in-an-array/
            

        
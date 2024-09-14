# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        binary = '0'
        while (head != None):
            binary = binary + str(head.val)
            head = head.next
        return int(binary, 2)
        
# complexidade de espaço: O(1)
# complexidade de tempo: O(n)

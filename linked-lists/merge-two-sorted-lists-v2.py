# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        output = ListNode()
        head = output

        while (list1 != None and list2 != None): 
            if (list1.val <=list2.val):
                output.next = list1 
                list1 = list1.next 
            else:
                output.next = list2 
                list2 = list2.next 
            output = output.next 
        if (list1 != None):
            output.next = list1
        if (list2 != None): 
            output.next = list2 
        return head.next

## complexidade de tempo: O (n+m)
## complexidade de espaço: O(1)
# https://leetcode.com/problems/merge-two-sorted-lists/






        
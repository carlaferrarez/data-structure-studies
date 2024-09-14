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
        if (list2 == None):
            return list1
        if (list1 == None):
            return list2

        if (list1.val <= list2.val):
            output = list1 ##output = 1
            list1 = list1.next ## list1 = [2,4]
        else:
            output = list2 ## -1
            list2 = list2.next ## list2 = 1
        head = output

        while (list1 != None and list2 != None): ## list1 = [2,4] list2 = [3,4]
            if (list1.val <=list2.val):
                output.next = list1 #output -1,0,1,2,4
                list1 = list1.next ## None
            else:
                output.next = list2 ##output = [1,1]
                list2 = list2.next ## list2 = [3,4]
            output = output.next
        if (list1 != None):
            output.next = list1
        if (list2 != None):
            output.next = list2 #output -1,0,1,2,4,5

        return head


## complexidade de tempo: O (n+m)
## complexidade de espaço: O(1)
## https://leetcode.com/problems/merge-two-sorted-lists/






        
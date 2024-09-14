# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if (head == None):
            return head
        if (head.next == None):
            return head
        size = self.countElements(head)
        middle = size // 2
        current_node = head
        count = 0
        while (count < middle): 
            current_node = current_node.next 
            count = count + 1 
        return current_node

    def countElements(self, current_node):
        size = 1
        while (current_node.next != None):
            size = size + 1
            current_node = current_node.next
        return size

## complexidade de espaco = O(1)
## complexidade de tempo = 0(n)
# https://leetcode.com/problems/middle-of-the-linked-list/
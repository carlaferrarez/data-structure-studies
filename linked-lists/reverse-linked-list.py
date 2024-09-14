# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if (head == None or head.next == None):
            return head
        current_node = head
        previous_node = None
        while (current_node != None): # 1 2, 3
            next_node = current_node.next # 2, 3, none
            current_node.next = previous_node # 1 -> None, 2 -> 1, 3 -> 2

            previous_node = current_node  # 1, 2, 3
            current_node = next_node  # 2, 3, none

        return previous_node
# complexidade de espaco O(1)
# complexidade de tempo O(n)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        previous_node = head ## 1 
        current_node = head ## 1

        while (current_node != None):
            if (current_node.val == val):  ## 
                if (previous_node.val == current_node.val):
                    if (current_node == head):
                        head = head.next ##  
                    else:
                        current_node = head ## gambiarra?
                else:
                    previous_node.next = current_node.next ## [1,2,1]
            previous_node = current_node ##  1, 2 
            current_node = current_node.next ##  2, 22,
        return head ##[1,2, 1]

## complexidade de tempo: O(n)
## complexidade de espaço: O(1)
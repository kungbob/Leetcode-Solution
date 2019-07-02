# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        start = ListNode(None)
        start.next = head
        prev = start
        while head != None:
            if head.val == val:
                prev.next = head.next
            else:
                prev = head
            head = head.next
            
        return start.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        appear = []
        start = ListNode(None)
        start.next = head
        pre = start
        while head is not None:
            if head.val in appear:
                pre.next = head.next
                
            else:
                appear.append(head.val)
                pre = head
            head = head.next
        return start.next
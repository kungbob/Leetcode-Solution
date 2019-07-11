# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        temp = head
        length = 0
        while temp is not None:
            length += 1
            temp = temp.next
        middle = length // 2
        loop = head
        while middle != 0:
            loop = loop.next
            middle -= 1
            
        return loop
        
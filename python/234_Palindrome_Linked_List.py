# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        
        fast = head
        slow = head
        
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        current = slow
        while current != None:
            temp = current
            current = current.next
            temp.next  = prev
            prev = temp
            
        while prev != None:
            if prev.val != head.val:
                return False
            else:
                head = head.next
                prev = prev.next
                
        return True
        
        
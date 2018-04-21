# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        """
        list_1 = []
        list_2 = []
        while l1:
            list_1.append(l1.val)
            l1 = l1.next
        while l2:
            list_2.append(l2.val)
            l2 = l2.next
        sum_1 = 0
        sum_2 = 0
        for i in range(0, len(list_1)):
            sum_1 += list_1[i] * pow(10, i)

        for i in range(0, len(list_2)):
            sum_2 += list_2[i] * pow(10, i)
        total = sum_1 + sum_2

        list_node = ListNode(total % 10)
        start_node = list_node
        while total > 9:
            total = total // 10
            list_node.next = ListNode(total % 10)
            list_node = list_node.next


        return start_node
        """

        # Improved version
        # Iterate and Add in the same time

        carry = 0
        sum = 0
        list_node = ListNode(sum % 10)
        start_node = list_node
        while l1:
            if l2:
                sum = l1.val + l2.val + carry
                carry = sum // 10
                l2 = l2.next
            else:
                sum = l1.val + carry
                carry = sum // 10

            list_node.next = ListNode(sum % 10)
            list_node = list_node.next

            l1 = l1.next

        while l2:
            sum = l2.val + carry
            carry = sum // 10
            list_node.next = ListNode(sum % 10)
            list_node = list_node.next

            l2 = l2.next

        if carry:
            list_node.next = ListNode(carry % 10)
            list_node = list_node.next


        return start_node.next

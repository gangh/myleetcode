# -*- coding:utf-8 -*-


# Given a linked list, remove the n-th node from the end of list and return its head.
#
# Example:
#
#
# Given linked list: 1->2->3->4->5, and n = 2.
#
# After removing the second node from the end, the linked list becomes 1->2->3->5.
#
#
# Note:
#
# Given n will always be valid.
#
# Follow up:
#
# Could you do this in one pass?
#


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        def get_len_of_linkedlist(head):
            length = 1
            while head.next:
                head = head.next
                length += 1
            return length
        list_length = get_len_of_linkedlist(head)
        position = list_length - n
        if list_length == 1:
            return None
        if position==0:
            return head.next
        head_p = head
        for i in range(position-1):
            head_p = head_p.next
        head_p.next = head_p.next.next
        return head

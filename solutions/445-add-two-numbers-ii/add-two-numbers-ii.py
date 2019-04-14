# -*- coding:utf-8 -*-


# You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Follow up:
# What if you cannot modify the input lists? In other words, reversing the lists is not allowed.
#
#
#
# Example:
#
# Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 8 -> 0 -> 7
#
#


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # hard way ,transfer to int
        def node2int(node):
            num_list=[str(node.val)]
            while node.next:
                node = node.next
                num_list.append(str(node.val))
            num_s = ''.join(num_list)
            print num_s
            return int(num_s)
        
        sumed = node2int(l1)+node2int(l2)
        
        def int2node(int_num):
            str_list = list(str(int_num))
            head_node = ListNode(int(str_list[0]))
            last_node = head_node
            for i in range(1,len(str_list)):
                node = ListNode(int(str_list[i]))
                last_node.next = node
                last_node = node
            return head_node
        return int2node(sumed)
        # there is a granceful way by add leading zeros

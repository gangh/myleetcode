# -*- coding:utf-8 -*-


# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8


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
        list_1 = self.list_linked_nodes(l1)
        list_2 = self.list_linked_nodes(l2)
        number_1 = self.get_number_from_list(reversed(list_1))
        number_2 = self.get_number_from_list(reversed(list_2))
        number = number_1 + number_2
        return self.get_list_from_number_reversed(number)
        
        
    def get_list_from_number_reversed(self,number):
        num_str_list = list(str(number))
        number_node_list = [ListNode(int(i)) for i in num_str_list]
        number_node_list.reverse()
        for index,item in enumerate(number_node_list):
            try:
                item.next = number_node_list[index+1]
            except IndexError as e:
                return number_node_list[0]
            
    def get_number_from_list(self,number_list):
        return int(''.join([str(i.val) for i in number_list]))

    def list_linked_nodes(self,first_item_in_singly_linked_list):
        list_of_items = []
        now_item = first_item_in_singly_linked_list
        while True:
            list_of_items.append(now_item)
            if now_item.next is None:
                return list_of_items
            now_item = now_item.next

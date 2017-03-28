# -*- coding:utf-8 -*-


# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
#
# Example:
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index_1,number_1 in enumerate(nums):
            for index_2,number_2 in enumerate(nums[index_1 + 1 :]):
                if number_1 + number_2 == target:
                    return [index_1,index_2 + index_1 + 1]

# -*- coding:utf-8 -*-


# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
#
#
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
#
# For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.
#
# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
#
#
# 	I can be placed before V (5) and X (10) to make 4 and 9. 
# 	X can be placed before L (50) and C (100) to make 40 and 90. 
# 	C can be placed before D (500) and M (1000) to make 400 and 900.
#
#
# Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.
#
# Example 1:
#
#
# Input: 3
# Output: "III"
#
# Example 2:
#
#
# Input: 4
# Output: "IV"
#
# Example 3:
#
#
# Input: 9
# Output: "IX"
#
# Example 4:
#
#
# Input: 58
# Output: "LVIII"
# Explanation: L = 50, V = 5, III = 3.
#
#
# Example 5:
#
#
# Input: 1994
# Output: "MCMXCIV"
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
#


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        s_l = ['I','X','C','M']
        s_l_half = ['V','L','D']
        n_l = list(str(num))
        empty_list = []
        for k,v in  enumerate(reversed(n_l)):
            v = int(v)
            if v <= 3:
                s_item  = s_l[k]*v
            elif v == 4:
                s_item = s_l[k] + s_l_half[k]
            elif v <=8 :
                s_item = s_l_half[k] + s_l[k]*(v-5)
            elif v==9:
                s_item = s_l[k] + s_l[k+1]
            empty_list.append(s_item)
        out_list = reversed(empty_list)
        return ''.join(out_list)

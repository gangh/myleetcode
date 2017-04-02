# -*- coding:utf-8 -*-


# Reverse digits of an integer.
#
#
# Example1: x =  123, return  321
# Example2: x = -123, return -321
#
#
# click to show spoilers.
#
# Have you thought about this?
#
# Here are some good questions to ask before coding. Bonus points for you if you have already thought through this!
#
# If the integer's last digit is 0, what should the output be? ie, cases such as 10, 100.
#
# Did you notice that the reversed integer might overflow? Assume the input is a 32-bit integer, then the reverse of 1000000003 overflows. How should you handle such cases?
#
# For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
#
#
#
#
#
# Note:
# The input is assumed to be a 32-bit signed integer. Your function should return 0 when the reversed integer overflows.


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
            prefix = ''
        else:
            prefix = '-'
        x=abs(x)
        x_list = list(str(x))
        x_list.append(prefix)
        x_list.reverse()
        reversed_x = int(''.join(x_list))
        return self.int_overflow(reversed_x)
            
    def int_overflow(self,val):  
        maxint = 2147483647  
        if not -maxint-1 <= val <= maxint:  
            val = 0
        return val  

# -*- coding:utf-8 -*-


# Implement atoi which converts a string to an integer.
#
# The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.
#
# The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.
#
# If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.
#
# If no valid conversion could be performed, a zero value is returned.
#
# Note:
#
#
# 	Only the space character ' ' is considered as whitespace character.
# 	Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
#
#
# Example 1:
#
#
# Input: "42"
# Output: 42
#
#
# Example 2:
#
#
# Input: "   -42"
# Output: -42
# Explanation: The first non-whitespace character is '-', which is the minus sign.
#              Then take as many numerical digits as possible, which gets 42.
#
#
# Example 3:
#
#
# Input: "4193 with words"
# Output: 4193
# Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
#
#
# Example 4:
#
#
# Input: "words and 987"
# Output: 0
# Explanation: The first non-whitespace character is 'w', which is not a numerical 
#              digit or a +/- sign. Therefore no valid conversion could be performed.
#
# Example 5:
#
#
# Input: "-91283472332"
# Output: -2147483648
# Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
#              Thefore INT_MIN (−231) is returned.
#


class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        l = []
        negative_appeared = False
        number_appeared = False
        positive_appeared = False
        white_space_appeared = False
        for char in str:
            if  char==' ' or (char=='0' and not number_appeared) or char=='+':
                if char == '0':
                    number_appeared=True
                if char=='+': 
                    if negative_appeared or positive_appeared:
                        break
                    positive_appeared=True

                if char == ' ' and number_appeared: white_space_appeared=True
                if char == ' ' and (positive_appeared or negative_appeared)and not number_appeared:
                    return 0
                continue
            elif char.isdigit():
                if number_appeared and white_space_appeared:
                    break
                l.append(char)
                number_appeared = True
            elif  char=='-':
                if number_appeared or negative_appeared or positive_appeared:
                    break
                else:
                    negative_appeared = True
                    l.append(char)
                    continue
            else:
                break
        num_str = ''.join(l)
        if num_str and (num_str!='-') and (num_str!='+'):
            num = int(num_str)
        else:
            return 0
        # it is stupid !!!
        return max(-2**31, min(num,2**31-1))


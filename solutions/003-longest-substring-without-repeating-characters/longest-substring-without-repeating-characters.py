# -*- coding:utf-8 -*-


# Given a string, find the length of the longest substring without repeating characters.
#
#
# Example 1:
#
#
# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 
#
#
#
# Example 2:
#
#
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
#
#
#
# Example 3:
#
#
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
#              Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
#
#
#
#


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length = 0
        max_allow_length = len(set(s))+1
        for index,word in enumerate(s):
            # 对每个匹配长度由 最大长 至 最长不重复长
            for length,end_index in enumerate(range(index+max_length,index+max_allow_length)):
                # 此判断检查是否为无重复的字符串
                sub_str = s[index:end_index]
                sub_str_length = len(sub_str)
                if len(set(sub_str)) == sub_str_length:
                   if sub_str_length > max_length:
                       max_length = sub_str_length
                       if max_length == max_allow_length-1:
                           return max_length
                else:
                    break
        return max_length

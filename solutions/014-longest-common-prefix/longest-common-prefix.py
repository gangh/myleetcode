# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
#
# Example 1:
#
#
# Input: ["flower","flow","flight"]
# Output: "fl"
#
#
# Example 2:
#
#
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
#
#
# Note:
#
# All given inputs are in lowercase letters a-z.
#


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix_s_l = []
        if not strs:
            return ''
        try:
            for position,c in enumerate(strs[0]):
                for s_l in strs:
                    if s_l[position] != c:
                        return ''.join(prefix_s_l)
                prefix_s_l.append(c)
        except IndexError:
            return ''.join(prefix_s_l)
        return ''.join(prefix_s_l)
                    

# -*- coding:utf-8 -*-


# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
#
#
# P   A   H   N
# A P L S I I G
# Y   I   R
#
#
# And then read line by line: "PAHNAPLSIIGYIR"
#
# Write the code that will take a string and make this conversion given a number of rows:
#
#
# string convert(string s, int numRows);
#
# Example 1:
#
#
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
#
#
# Example 2:
#
#
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
#
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
#


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows <= 1: return s
        matrix = [[] for i in range(numRows)]
        columns = 0
        row_index = 0
        for char_i in list(s):
            modulo = columns%(numRows-1)
            if modulo == 0:
                matrix[row_index].append(char_i)
                row_index += 1
            elif modulo != 0:
                for row in range(numRows):
                    if  (numRows-row-1) == modulo:
                        matrix[row].append(char_i)
                    # else:
                    #     matrix[row].insert(columns, None)
                columns += 1
            if row_index==numRows:
                columns += 1
                row_index = 0
        
        # matrix_without_none = [[i for i in l if i] for l in matrix]
        long_list = reduce(lambda x,y: x+y,matrix,[])
        merged_string = ''.join(long_list)
        return merged_string
            


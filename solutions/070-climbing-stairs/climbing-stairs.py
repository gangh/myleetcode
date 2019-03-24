# -*- coding:utf-8 -*-


# You are climbing a stair case. It takes n steps to reach to the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#
# Note: Given n will be a positive integer.
#
# Example 1:
#
#
# Input: 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
#
#
# Example 2:
#
#
# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
#
#


import math

class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        assert(isinstance(n,int))
        assert(n>0)
        
        ways=0
        if n%2==0:
            start_count=0
        else:
            start_count=1

        for m_1 in range(start_count,n+1,2):
            # the count of num n 1 step is from 0 to n interval 2,when count of step 1 is m_1,the count of step of 2 is m_2   so,the ways is C(m_1,m_1+m_2)
            m2=int((n-m_1)//2)
            all_item_count = int(n-m2)
            ways_count=int(math.factorial(all_item_count))//(int(math.factorial(m_1))*int(math.factorial(m2)))
            ways += int(ways_count)
        return ways 

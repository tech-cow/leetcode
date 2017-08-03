#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Yu Zhou
# 453. Minimum Moves to Equal Array Elements


# 找到当前值和最小值的差，记录一个counter
class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        #minu = min(nums)
        for num in nums:
            count += num - minu
        return count



# 第一次的试验，TLE
# 思路是每次进行一次sort，然后更改N-1的值
class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        if len(nums) == 2:
            return max(nums) - min(nums)

        while not self.allEqual(nums):
            nums = sorted(nums)
            for num in xrange(len(nums)-1):
                num += 1
            count += 1
        return count




    def allEqual(self, nums):
        return len(set(nums)) <= 1

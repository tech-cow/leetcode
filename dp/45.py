#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Yu Zhou
# 45. Jump Game

# DP, 超时
# O(N^2)
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Create DP
        dp = [float('inf') for i in xrange(len(nums))]

        dp[0] = 0

        # Function
        for i in xrange(len(nums)):
            for j in xrange(i):
                #当在j这个节点，跳nums[j]个位置，大于等于目前所在的i节点上的话，那么我们对dp[i]进行增量
                if nums[j] + j >= i:
                    dp[i] = min(dp[i], dp[j] + 1)

        return dp[-1]

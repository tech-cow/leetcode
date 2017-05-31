#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Yu Zhou
# 53. Maximum Subarray

# DP的思路是比对dp[i-1]+nums[i] 和nums[i]本身的值
# 状态：从之前一个节点到现在节点的最大值

# DP
# O(N)

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        dp = [float('-inf') for i in xrange(len(nums))]
        res = dp[0] = nums[0]

        for i in xrange(1, len(nums)):
            dp[i] = max(nums[i]+dp[i-1], nums[i])
            res = max(res, dp[i])

        return res

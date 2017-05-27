#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Yu Zhou
# 300. Longest Increasing Subsequence

# DP O(N^2)
# 状态：到目前f[i]点为止，经过比较，从 0 ->i 最大的 的List
# 方程： if num[i] > num[j] :
#         get the max of (dp[i], dp[j]+1)  因为dp[i]很可能会比dp[j]+1 大


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Edge
        if not nums:
            return 0

        # Creating DP
        dp = [1 for i in xrange(len(nums))]

        for i in xrange(len(nums)):
            for j in xrange(i):
                if nums[j] < nums[i]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1

        return max(dp)

#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Yu Zhou
# 198. House Robber

# DP的思路是比对dp[i-2]+nums[i] 和dp[i-1]的值
# 状态：从0到i，不能选择相邻节点得到的最大值

# DP
# 时间/空间 O(N)

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        数学公式
        f(0) = nums[0]
        f(1) = max(f(0), f(1))
        f(2) = max(nums(2)+ f(0), f(1))
        f(3) = max(nums(3)+ f(1), f(2))
        .
        .
        f(n) = max(nums(n) + f(n-2), f(n-1))
        """
        # Edge
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]


        # Creating dp
        dp = [0 for i in xrange(len(nums))]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        # DP
        for i in xrange(2, len(nums)):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])

        return dp[-1]

#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Yu Zhou
# 55. Jump Game

# DP的思路是创建一个DP的Array用来存储Boolean
# 状态：在每个节点，比对之前的所有节点，若之前节点为True且之前节点拥有到达目前且超过目前index的能力
# 那么就实现

# DP, TLE
# O(N^2)
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #Edge
        if not nums:
            return True

        dp = [False for i in xrange(len(nums))]

        dp[0] = True

        for i in xrange(len(nums)):
            for j in xrange(i):
                if dp[j] and j + nums[j] >= i:
                    dp[i] = True
                    break

        print dp
        return dp[-1]

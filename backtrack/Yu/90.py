#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Yu Zhou

# 90. Subsets II
# Given a collection of integers that might contain duplicates, nums, return all possible subsets.

# 思路
# 在之前的subset I 的基础上做一个condition check

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        def dfs(nums, temp, index):
            self.res.append(temp[:])
            for i in xrange(index, len(nums)):
                # Check for index bound, and remove duplicate
                if i > index and nums[i] == nums[i-1]:
                    continue
                temp.append(nums[i])
                dfs(nums, temp, i + 1)
                temp.pop()
        dfs(sorted(nums), [], 0)
        return self.res

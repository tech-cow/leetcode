#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Yu Zhou

# 46. Permutations
# Given a collection of distinct numbers, return all possible permutations.



# 思路
# 基础地轨思路

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        def dfs(nums, temp):
            if len(temp) == len(nums):
                self.res.append(temp[:])

            for i in xrange(len(nums)):
                if nums[i] in temp:
                    continue
                temp.append(nums[i])
                dfs(nums, temp)
                temp.pop()
        dfs(nums, [])
        return self.res
        

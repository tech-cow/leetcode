#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Yu Zhou
# Youtube: https://youtu.be/imLl2s9Ujis

# 47. Combinations

# 这题超时了，但思路没错。。。。
# 搞不定。。

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        nums = []
        for i in xrange(1, n+1):
            nums.append(i)

        self.res = []
        self.used = [False] * len(nums)
        def dfs(nums, temp, index):
            if len(temp) == k:
                self.res.append(temp[:])
                return


            for i in range(index, len(nums)):
                if self.used[i]: continue

                self.used[i] = True
                temp.append(nums[i])
                dfs(nums, temp, i)
                temp.pop()
                self.used[i] = False

        dfs(nums, [], 0)
        return self.res

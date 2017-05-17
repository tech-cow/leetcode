#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Yu Zhou
# Youtube: https://youtu.be/imLl2s9Ujis

# 46. Permutations
# 这道题改动了3点
# 1. 把数组变成了sorted，因为我们要对index前后的数进行处理
# 2. 当前数如果和之前的一样  以及
# 3. 之前的值已经进行递归了话， 我们跳过当前的值。


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        self.used = [False] * len(nums)

        def dfs(nums, temp):
            if len(temp) == len(nums):
                self.res.append(temp[:])

            for i in xrange(len(nums)):
                if self.used[i]: continue

                if i>0 and nums[i] == nums[i-1] and self.used[i - 1]: continue
                self.used[i] = True
                temp.append(nums[i])
                dfs(nums, temp)
                self.used[i] = False
                temp.pop()
        dfs(sorted(nums), [])
        return self.res

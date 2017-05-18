#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Yu Zhou

# 216. Combination Sum III

# 比Combination Sum难度要Easy一些
# 思路就是注意剪枝

class Solution(object):
    def combinationSum3(self, size, target):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.res = []

        def dfs(size, remainder, temp, index):
            if len(temp) == size and remainder == 0:
                self.res.append(temp[:])
            #剪枝
            if len(temp) > size:
                return
            for i in xrange(index, 10):
                temp.append(i)
                dfs(size, remainder - i, temp, i + 1)
                temp.pop()
        dfs(size, target, [], 1)
        return self.res

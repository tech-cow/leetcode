#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Yu Zhou
# 463. Island Perimeter

# 将所有的1，也就是所有的格子乘以4，储存在一个res的变量
# 检查这个格子的邻居，有则在变量减去2

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        for i in xrange(len(grid)):
            for j in xrange(len(grid[i])):
                if grid[i][j] == 1:
                    res += 4
                    # Check Neighbor
                    if i>0 and grid[i-1][j] == 1:
                        res -= 2
                    if j>0 and grid[i][j-1] == 1:
                        res -= 2
        return res

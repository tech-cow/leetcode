#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Yu Zhou
# 452. Minimum Number of Arrows to Burst Balloons

# 用到了Greedy的一个，扫描线的运用
# 先进行排序，然后在每次循环的时候
# 比对end point，然后更新end point，若超出end point范围，则增加一个arrow
# 这道题的知识点是扫描线+ 如何sort 一个tuple里面的第一个值

class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        points = sorted(points, key = lambda x: x[1])
        end = -float('inf')
        res = 0
        for ballon in points:
            if ballon[0] > end:
                end = ballon[1]
                res += 1
        return res

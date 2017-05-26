#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Yu Zhou
# 62. Unique Path

# 解题思路：
# 先解决横向竖向第一列，全部设成1，用了个小trick把所有的DP矩阵都设成了1
# 状态：计算从前到现在节点为止所有的路劲
# 状态转移方程：f[x][y] = f[x-1][y] + f[x][y-1]
# 最后返回右下角的数就行。

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        #edge:
        if not m or not n:
            return 0

        dp = [[1 for _ in range(n)] for _ in range(m)]

        for i in xrange(1, m):
            for j in xrange(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[-1][-1]

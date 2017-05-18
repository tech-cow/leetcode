#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Yu Zhou
# 60. Permutation Sequence

#思路
# 这题超时了，LeetCode里面有一种数学的解法
# 就不深究了，这种数学的解法就是看人品了
# 以下代码是可以用的，就是过不了LC的Test Case
# 思路和Permutation差不多，只是不是对array，而是对String的操作。

class Solution(object):
    def getPermutation(self, size, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """

        # We need to traverse to the level of size , get all of the different permutation
        # and return the kth element within all permutation

        self.res = []

        def dfs(size, strr):
            if len(strr) == size :
                    self.res.append(strr)

            for i in xrange(1, size+1):
                if str(i) in strr: continue

                strr += str(i)
                dfs(size, strr)
                strr = strr[:-1]
        dfs(size, "")
        #print self.res
        return self.res[k-1]

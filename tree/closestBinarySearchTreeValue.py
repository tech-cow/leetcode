#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Wei Dai

# ****************
# Descrption:
# 270. Closest Binary Search Tree Value

#Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.
# ****************

# 思路：
# BST上二分搜索 把partial optimal和root自己的值进行比较取最优

# ****************
# Final Solution *
# ****************
class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        if not root:
            return -1
        if not root.left and not root.right:
            return root.val
            
        cur = root.val
        if target > cur:
            halfOpt = self.closestValue(root.right, target)
        else:
            halfOpt = self.closestValue(root.left, target)
        cDif, hDif = abs(cur - target), abs(halfOpt - target)
        res = cur if cDif < hDif else halfOpt
        return res

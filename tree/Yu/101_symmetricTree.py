#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Yu Zhou
# ****************
# Descrption:
# 101. Symmetric Tree
# Given a binary tree, check whether it is a mirror of itself
# (ie, symmetric around its center).
# ****************

# 思路：
# 这道题只要知道一个规律,就是左边Child要等于右边Child，就很容易了
# 先解决Root的Edge，之后在对其他进行一个统一处理，我选择写一个Helper，也可以不写

# if not left or not right: return left == right的意思是：
        # if not left or not right: return False
        # if not left and not right: return True

class Solution(object):
    def isSymmetric(self, root):

        if not root: return True
        def dfs(left, right):
            if not left or not right: return left == right
            if left.val != right.val: return False
            return dfs(left.left, right.right) and dfs(left.right, right.left)

        return dfs(root.left, root.right)

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
# ****************
# Final Solution *
#   Recursive    *
# ****************
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        else:
            return self.isEqual(root.left, root.right)

    def isEqual(self, n1, n2):
        if not n1 or not n2:
            return n1 == n2
        else:
            return n1.val == n2.val and self.isEqual(n1.left, n2.right) and self.isEqual(n1.right, n2.left)

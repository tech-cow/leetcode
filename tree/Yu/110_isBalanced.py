#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Yu Zhou

# ****************
# Descrption:
# 110. Balanced Binary Tree
# Given a binary tree, determine if it is height-balanced.
# ****************

# 思路：
# 这道题，写一个Helper用来返回树的高度
# 有个小技巧，因为题目告诉高度一定是正数，所以我们可以用 -1 来表示两边的高差大于1，也就是不对等
# 先左右递归， 每一层的比对条件是：下一层Sub Tree传上来的值有没有 -1，
# 有的话说明Sub Tree开始就有不对等，那么就一直向上返回-1
# 若没有 -1， 则比较现在这一层的高度差是否有超过一，同理向上递归
# 当最后得到一个值返回给主方程，在比对是否是1，返回Bool。


# ****************
# Final Solution *
# ****************
class Solution(object):
    def isBalanced(self, root):
        #Edge Case
        if not root:
            return True
        else:
            return self.maxDepth(root) is not -1

    def maxDepth(self, root):
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return 1 + max(left ,right)

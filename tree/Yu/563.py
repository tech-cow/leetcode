#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Yu Zhou

# ****************
# Descrption:
# 563. Binary Tree Tilt
# Given a binary tree, return the tilt of the whole tree.
# The tilt of a tree node is defined as the absolute difference between the sum of all left subtree node values and the sum of all right subtree node values. Null node has tilt 0.
# The tilt of the whole tree is defined as the sum of all nodes' tilt.
# ****************

# 思路：
# 每层处理的事情就是增加Global Variable的变量
# 然后返回左右两边以及本身的Sum

# ****************
# Final Solution *
# ****************
class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        def helper(root):
            if not root:
                return 0
            left = helper(root.left)
            right = helper(root.right)
            self.res += abs(left - right)
            return root.val + left + right
        helper(root)
        return self.res

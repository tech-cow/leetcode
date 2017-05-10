#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Yu Zhou
# ****************
# Descrption:
# 112. Path Sum
# Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
# ****************

# 思路
# 每次向下递归要确保root.left和root.right都是None
# 像上返回的时候对Sum和Root.Val进行比对

# 本人的中文视频讲解：
# https://www.youtube.com/watch?v=LgtcGjIuE18&feature=youtu.be



# ****************
# Final Solution *
# ****************
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        #Edge
        if not root:
            return False

        #Process
        if not root.left and not root.right:
            return sum - root.val == 0
        else:
            sum -= root.val

        #Recursion
        left = self.hasPathSum(root.left, sum)
        right = self.hasPathSum(root.right, sum)

        return left or right

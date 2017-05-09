#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Yu Zhou

# ****************
# Descrption:
# 543. Diameter of Binary Tree
# Given a binary tree, you need to compute the length of the diameter of the tree.
# The diameter of a binary tree is the length of the longest path between any two
# nodes in a tree. This path may or may not pass through the root.
# ****************

# 思路：
# 这题最重要是写一个global sum用来比对当前最大的长度，和之前保存的最大的长度
# 因为可能subtree某个长度会高于从外围root的长度

# 本人的中文视频讲解：
# https://www.youtube.com/watch?v=0VnOfu2pYTo

# ****************
# Final Solution *
# ****************
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #Global MAX
        self.max = 0

        #返回目前节点的最大值，以及对全球变量的返回值进行比对，更改
        def currentMax(root):
            #Edge:
            if not root:
                return 0

            # Divide and Conquer
            # 左右节点返回一个当前为止的最大值
            left = currentMax(root.left)
            right = currentMax(root.right)

            self.max = max(self.max, left + right)

            # 像上层返回左右两边取舍的最大值
            return 1 + max(left, right)

        currentMax(root)
        return self.max

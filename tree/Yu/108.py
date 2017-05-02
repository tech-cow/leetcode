#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Yu Zhou

# ****************
# 108. Convert Sorted Array to Binary Search Tree
# Descrption:
# Given an array where elements are sorted in ascending order,
# convert it to a height balanced BST.
# ****************

# 思路：
# 基础递归
# 每层的任务是，创建mid节点。

# ****************
# Final Solution *
# ****************
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        #Edge:
        if not nums:
            return None

        mid = len(nums) / 2

        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])

        return root

# ***************************************
# The following code is an fail attempt *
# ***************************************

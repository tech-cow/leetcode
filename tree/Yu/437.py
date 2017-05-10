#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Yu Zhou
# 437. Path Sum III

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """

        # Edge Case:
        if not root:
            return 0

        # Process
        def dfs(root, sum):
            count = 0

            if not root:
                return 0
            if root.val == sum:
                count += 1

            count += dfs(root.left, sum - root.val)
            count += dfs(root.right, sum -root.val)
            return count

        # Recursion
        return dfs(root,sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
